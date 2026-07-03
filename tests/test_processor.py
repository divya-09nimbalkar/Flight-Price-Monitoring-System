import pandas as pd
from src.processor import clean_data

def test_clean_data():
    df = pd.DataFrame({
        "date": ["2024-01-01", None],
        "price": [4500, None],
        "volume": [10, None]
    })
    cleaned = clean_data(df)
    assert cleaned.isnull().sum().sum() == 0
    assert cleaned["price"].dtype == float
