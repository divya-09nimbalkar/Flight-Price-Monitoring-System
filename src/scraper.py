import pandas as pd
from pathlib import Path

def fetch_mock_flights() -> pd.DataFrame:
    data_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "flights.csv"
    return pd.read_csv(data_path)

