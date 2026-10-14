import os
import time
from dotenv import load_dotenv
from scraper import CryptoScraper
from utils import save_to_csv

load_dotenv()

API_KEY = os.getenv("CMC_API_KEY", "e97bc1bbe52a48c39518935ac9c1dc82")
API_URL = os.getenv("CMC_API_URL", "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest")
CSV_PATH = os.getenv("CSV_FILE_PATH", r"E:\Python project\API.CSV")
FETCH_LIMIT = int(os.getenv("FETCH_LIMIT", 10))


def run_pipeline(scraper: CryptoScraper):
    try:
        print("\n[*] Mengambil data terbaru dari CoinMarketCap...")
        raw_data = scraper.fetch_latest_listings(limit=FETCH_LIMIT)
        df = scraper.process_data(raw_data)
        
        print(f"[+] Berhasil memproses {len(df)} item cryptocurrency.")
        save_to_csv(df, CSV_PATH)
        
    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")


def main():
    scraper = CryptoScraper(api_key=API_KEY, api_url=API_URL)
    
    max_iterations = 333
    delay_seconds = 60

    print("=== Crypto Data Scraper Started ===")
    
    for i in range(1, max_iterations + 1):
        print(f"\n--- Iterasi ke-{i} dari {max_iterations} ---")
        run_pipeline(scraper)
        
        if i < max_iterations:
            print(f"[*] Menunggu {delay_seconds} detik sebelum pengambilan berikutnya...")
            time.sleep(delay_seconds)

    print("\n=== Proses Selesai ===")


if __name__ == "__main__":
    main()