import pandas as pd
from src.analytics import run_analysis

def test_run_analysis():
    df = pd.DataFrame({
        "date": ["2024-01-01","2024-01-02"],
        "price": [4500, 3800],
        "volume": [10, 20]
    })
    results = run_analysis(df)
    assert "avg_price" in results
    assert results["min_price"] == 3800
