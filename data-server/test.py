import logging as log
from flask import Flask, Response, request
from pandas import read_csv
from pathlib import Path


app = Flask(__name__)

DATA_PATH: Path = Path("./data/gds.csv")
TIME_COLUMN: str = "Time"


def get_data():
    try:
        df = read_csv(DATA_PATH)
        
        print(df)

    except Exception as e:
        log.error(e)


if __name__ == "__main__":
    get_data()
