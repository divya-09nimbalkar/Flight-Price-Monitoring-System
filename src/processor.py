import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean flight data."""
    df = df.dropna()
    df["price"] = df["price"].astype(float)
    df["date"] = pd.to_datetime(df["date"])
    return df
