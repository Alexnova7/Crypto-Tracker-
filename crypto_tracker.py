import requests
import pandas as pd
import sqlite3
import time
import os
from datetime import datetime

def run_crypto_pipeline():
    # 1. EXTRACT
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,solana,binancecoin,ripple,cardano',
        'order': 'market_cap_desc'
    }
    
    try:
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Connecting to Global Market API...")
        res = requests.get(url, params=params)
        data = res.json()
        
        # 2. TRANSFORM
        df = pd.DataFrame(data)
        df = df[['name', 'symbol', 'current_price', 'price_change_percentage_24h']]
        df.columns = ['Asset', 'Ticker', 'Price_USD', 'Change_24h_%']
        
        # Sentiment logic
        df['Status'] = df['Change_24h_%'].apply(lambda x: "🚀 BULLISH" if x > 0 else "📉 BEARISH")
        df['Time'] = datetime.now().strftime("%H:%M:%S")

        # 3. LOAD (Save to SQLite)
        with sqlite3.connect('crypto_vault.db') as conn:
            df.to_sql('market_data', conn, if_exists='append', index=False)
        
        # 4. OUTPUT (Terminalda çap etmək)
        print("="*65)
        print("         LIVE CRYPTO DATA INGESTION SUCCESSFUL")
        print("="*65)
        print(df[['Asset', 'Price_USD', 'Change_24h_%', 'Status']].to_string(index=False))
        print("="*65)
        print(f"SUCCESS: Data logged to 'crypto_vault.db' at {datetime.now().strftime('%H:%M:%S')}")
        print("Next update in 60 seconds... (Press Ctrl+C to stop)\n")

    except Exception as e:
        print(f"PIPELINE ERROR: {e}")

if __name__ == "__main__":
    while True:
        run_crypto_pipeline()
        time.sleep(60)
        
