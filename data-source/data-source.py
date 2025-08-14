import pandas as pd
from flask import Flask, request, Response
from pathlib import Path

app = Flask(__name__)

ds = Path("./data")
TIME_COLUMN = "time"  # epoch seconds column in your CSV

@app.route("/data")
def get_data():
    try:
        # Get parameters (Grafana sends them in ms)
        data = request.args.get("source", type=str)
        CSV_PATH = ds / f"{data}.log.csv"
        from_ms = request.args.get("from", type=int)
        to_ms = request.args.get("to", type=int)

        df = pd.read_csv(CSV_PATH)

        if from_ms is None or to_ms is None:
            return Response(df.to_csv(index=False), mimetype="text/csv")

        from_s = from_ms / 1000
        to_s = to_ms / 1000
        df_ = df[(df[TIME_COLUMN] >= from_s) & (df[TIME_COLUMN] <= to_s)]
        if not len(df_):
            if from_ms == to_ms:
                df_ = df.head(1)
            else: 
                df_ = df.tail(1)

        return Response(df_.to_csv(index=False), mimetype="text/csv")

    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3010)