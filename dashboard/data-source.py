import logging as log
import pandas as pd
import sys
from flask import Flask, Response, request, render_template
from pathlib import Path

app = Flask(__name__)

ds = Path("./data")
TIME_COLUMN = "time"
OFFSET = { "posix": 0, "gds": 0, "aisio": 0 }

@app.route("/")
def home():
    # Renders templates/index.html
    return render_template("index.html")

@app.route("/data")
def get_data():
    try:
        global OFFSET
        data = request.args.get("source", type=str)
        from_ms = request.args.get("from", type=int)
        to_ms = request.args.get("to", type=int)

        CSV_PATH = ds / f"{data}.log.csv"
        df = pd.read_csv(CSV_PATH)

        offset = OFFSET[data]

        if offset < 0:
            res = df.head(1)
        elif offset >= df.shape[0]:
            res = df.tail(1)
        else:
            res = df.iloc[[offset]]
        
        OFFSET[data] += 1

        return Response(res.to_csv(index=False), mimetype="text/csv")
    except Exception as e:
        log.error(e)
        return Response(None, 500)


@app.route("/reset")
def reset():
    global OFFSET
    OFFSET = { "posix": 0, "gds": 0, "aisio": 0 }
    return Response()


def setupLogging():
    logFormatter = log.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = log.getLogger()

    fileHandler = log.FileHandler("./data-source.log")
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel(log.INFO)
    rootLogger.addHandler(fileHandler)

    consoleHandler = log.StreamHandler(stream=sys.stderr)
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(log.ERROR)
    rootLogger.addHandler(consoleHandler)


if __name__ == "__main__":
    setupLogging()
    app.run(host="0.0.0.0", port=3010)
