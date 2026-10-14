import json
import ssl
import urllib.parse
import urllib.request
import certifi
import pandas as pd


class CryptoScraper:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url

    def fetch_latest_listings(self, start: int = 1, limit: int = 10, convert: str = "USD") -> dict:
       
        params = urllib.parse.urlencode({
            "start": str(start),
            "limit": str(limit),
            "convert": convert,
        })
        
        request = urllib.request.Request(
            f"{self.api_url}?{params}",
            headers={
                "Accept": "application/json",
                "X-CMC_PRO_API_KEY": self.api_key,
            },
        )
        
        context = ssl.create_default_context(cafile=certifi.where())
        
        with urllib.request.urlopen(request, context=context) as response:
            data = json.load(response)
            
        return data

    def process_data(self, raw_data: dict) -> pd.DataFrame:
   
        if "data" not in raw_data:
            raise ValueError("Respon API tidak memiliki kunci 'data'")

        df = pd.json_normalize(raw_data["data"])
        df["timestamp"] = pd.to_datetime("now")
        return df