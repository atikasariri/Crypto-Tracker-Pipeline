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
├── data/                  # Local directory for stored CSV outputs (git-ignored)
│   └── API.CSV            # Log file containing historical crypto data
│
├── notebooks/             # Directory for Jupyter Notebooks
│   └── crypto_scraper.ipynb  # Main pipeline notebook
│
├── .env.example           # Example template for environment variables
├── .gitignore             # Specifies files and directories ignored by Git
├── LICENSE                # Open-source license terms (MIT)
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
