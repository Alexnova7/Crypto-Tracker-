import requests
import pandas as pd
import sqlite3
import time
import os
from datetime import datetime

class CryptoPipeline:
    def __init__(self):
        self.url = "https://api.coingecko.com/api/v3/coins/markets"
        self.params = {
            'vs_currency': 'usd',
            'ids': 'bitcoin,ethereum,solana,binancecoin,ripple,cardano',
            'order': 'market_cap_desc'
        }
        self.db = 'crypto_vault.db'

    def fetch_data(self):
        try:
            response = requests.get(self.url, params=self.params, timeout=10)
            return response.json()
        except:
            return None

    def process_data(self, raw_data):
        if not raw_data: return None
        df = pd.DataFrame(raw_data)
        df = df[['name', 'symbol', 'current_price', 'price_change_percentage_24h']]
        df.columns = ['Asset', 'Ticker', 'Price_USD', 'Change_24h_%']
        df['Status'] = df['Change_24h_%'].apply(lambda x: "BULLISH" if x > 0 else "BEARISH")
        return df

    def save_to_db(self, df):
        try:
            with sqlite3.connect(self.db) as conn:
                df.to_sql('market_trends', conn, if_exists='append', index=False)
        except:
            pass

    def start(self):
        while True:
            raw = self.fetch_data()
            clean_df = self.process_data(raw)
            if clean_df is not None:
                self.save_to_db(clean_df)
                os.system('clear')
                print("--- GLOBAL CRYPTO INGESTION SYSTEM ---")
                print(f"Status: Active | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print("-" * 55)
                print(clean_df[['Asset', 'Price_USD', 'Change_24h_%', 'Status']].to_string(index=False))
                print("-" * 55)
                print("Action: Data logged to SQLite | Interval: 60s")
            time.sleep(60)

if __name__ == "__main__":
    CryptoPipeline().start()
