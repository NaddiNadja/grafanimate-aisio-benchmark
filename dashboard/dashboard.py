import logging as log
import sys
from flask import Flask, render_template
from pathlib import Path


app = Flask(__name__)

DATA_PATH: Path = Path("./data.csv")
TIME_COLUMN: str = "time"


@app.route("/")
def home():
    # Renders templates/index.html
    return render_template("index.html")


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
