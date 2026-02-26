# 💰 Real-Time Global Crypto ETL Pipeline

A professional Python-based Data Engineering project that automates the extraction, transformation, and loading (ETL) of cryptocurrency market data into an SQLite database.

## 🚀 Project Overview
This pipeline tracks the top cryptocurrencies in real-time, providing live insights directly in the terminal and storing historical data for future analysis.

### Key Features:
* **Automated Extraction:** Fetches live market data (Price, Change %, Volume) from the CoinGecko API.
* **Data Transformation:** Uses `Pandas` to clean data, format currency, and perform live sentiment analysis (Bullish/Bearish).
* **Persistent Storage:** Logs all processed data into a local `SQLite` database (`crypto_vault.db`).
* **Live Dashboard:** Displays a clean, professional market table in the terminal that updates every 60 seconds.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Libraries:** Pandas, Requests, SQLite3
* **Environment:** GitHub Codespaces (Developed entirely on Mobile)

## 📊 How it Looks
```text
Asset     Price_USD    Change_24h_%  Status
Bitcoin   68208.00     4.79          🚀 BULLISH
Ethereum  2062.83      8.98          🚀 BULLISH