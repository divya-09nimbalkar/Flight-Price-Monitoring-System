from src.scraper import fetch_mock_flights

def test_fetch_mock_flights():
    df = fetch_mock_flights()
    assert not df.empty
    assert "price" in df.columns
    assert "route" in df.columns
