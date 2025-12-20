import finnhub
import os
from dotenv import load_dotenv
from pathlib import Path
import requests
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR.parent / ".env"
load_dotenv(ENV_PATH)

# Your credentials
AlphaVintage_key = os.getenv("alpha_vintage")




# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={AlphaVintage_key}'
r = requests.get(url)
data = r.json()

df = pd.DataFrame(data)

print(df)
