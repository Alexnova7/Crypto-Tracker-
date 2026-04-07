cat << 'EOF' > README.md
# Real-Time Global Crypto ETL Pipeline

A professional Data Engineering project designed to extract, transform, and load live cryptocurrency market data into a local SQLite database using Python.

## Project Overview
This ETL (Extract, Transform, Load) pipeline tracks top cryptocurrencies in real-time. It provides a live dashboard directly in the terminal and archives historical market data for future analysis.

## Live Output Preview
When running, the system generates the following real-time report:

| Asset    | Price_USD | Change_24h_% | Status   |
|----------|-----------|--------------|----------|
| Bitcoin  | 68601.00  | -1.77        | BEARISH  |
| Ethereum | 2096.36   | -2.21        | BEARISH  |
| BNB      | 604.97    | -0.25        | BEARISH  |
| XRP      | 1.31      | -2.34        | BEARISH  |
| Solana   | 80.73     | -1.16        | BEARISH  |
| Cardano  | 0.24      | -2.98        | BEARISH  |

## Key Features
- **Automated Extraction:** Fetches live market data via the CoinGecko API.
- **Data Transformation:** Cleans and formats raw JSON data using Pandas.
- **Persistent Storage:** Logs all processed data into a local SQLite database (`crypto_vault.db`).
- **Live Terminal Dashboard:** Displays a clean market table that refreshes every 60 seconds.

## Tech Stack
- **Language:** Python 3
- **Libraries:** Pandas, Requests, SQLite3
- **Environment:** Developed on mobile via GitHub Codespaces

## How to Run
To start the pipeline, execute the following command:
`python3 cryptotracker.py`
EOF
git add README.md
git commit -m "README updated with table preview"
git push origin main>