import os
import pandas as pd


def save_to_csv(df: pd.DataFrame, file_path: str) -> None:
    
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False)
        print(f"[+] File CSV baru berhasil dibuat di: {file_path}")
    else:
        df.to_csv(file_path, mode="a", header=False, index=False)
        print(f"[+] Data berhasil ditambahkan ke: {file_path}")