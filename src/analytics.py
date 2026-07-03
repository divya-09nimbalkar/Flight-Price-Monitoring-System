import pandas as pd

def run_analysis(df: pd.DataFrame) -> dict:
    """Return basic stats."""
    return {
        "rows": len(df),
        "avg_price": float(df["price"].mean()),
        "min_price": float(df["price"].min()),
        "max_price": float(df["price"].max())
    }
