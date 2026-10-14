# **Crypto Tracker Pipeline**

CryptoTracker Pipeline is a Python-based data ingestion script designed to fetch, clean, and store real-time cryptocurrency price data and statistics from the CoinMarketCap API.

The pipeline processes raw nested JSON data into a structured tabular format using "pandas" and appends historical price records into a local CSV file for downstream data analysis and monitoring.


_**Features**_

- **Real-Time Data Fetching**: Directly connects to the CoinMarketCap Pro API endpoint.
- **Data Normalization**: Flattens nested JSON responses into structured "pandas" DataFrames.
- **Timestamp Tracking**: Automatically adds execution timestamps to track price history over time.
- **CSV Logging**: Appends newly fetched records to a persistent local CSV dataset without overwriting historical entries.


_**Project Structure**_

```text
crypto-tracker-pipeline/
│
├── data/                  # Local directory for stored data outputs (git-ignored)
│   ├── .gitkeep           # Keeps empty data directory tracked in Git
│   └── crypto_data.csv    # Generated historical crypto dataset (ignored)
│
├── logs/                  # Local execution log files (git-ignored)
│   └── .gitkeep
│
├── notebooks/             # Jupyter Notebooks for EDA & API experimentation
│   └── crypto_eda.ipynb   # Exploratory Analysis & Visualization
│
├── src/                   # Source code / Production pipeline scripts
│   ├── __init__.py
│   ├── scraper.py         # API fetching and data ingestion logic
│   └── utils.py           # Helper functions (e.g., logger, env loader)
│
├── .env.example           # Example template for environment variables (API Keys)
├── .gitignore             # Git ignore rules (ignores .env, data/*.csv, logs/*)
├── LICENSE                # Open-source license terms (e.g., MIT)
├── README.md              # Detailed project documentation
├── main.py                # Main execution script to run the full pipeline
└── requirements.txt       # Project dependencies & libraries
