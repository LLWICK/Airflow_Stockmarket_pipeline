import finnhub
import os
from dotenv import load_dotenv
from pathlib import Path
import requests
import pandas as pd
import json


def run_stockMarket_ETL():

    BASE_DIR = Path(__file__).resolve().parent
    ENV_PATH = BASE_DIR.parent / ".env"
    load_dotenv(ENV_PATH)

    # Your credentials
    AlphaVintage_key = os.getenv("alpha_vintage")




    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={AlphaVintage_key}'
    r = requests.get(url)
    data = r.json()

    data1= data["Time Series (Daily)"] 

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(data1, orient="index")

    # Rename columns (remove numeric prefixes)
    df.columns = ["open", "high", "low", "close", "volume"]

    df["open"] = df["open"].astype("float")
    df["high"] = df["high"].astype("float")
    df["low"] = df["low"].astype("float")
    df["close"] = df["close"].astype("float")
    df["volume"] = df["volume"].astype("int")


    df.to_csv("s3://linal-stockmarket-airflow/IBM_stocks.csv", index=False)



