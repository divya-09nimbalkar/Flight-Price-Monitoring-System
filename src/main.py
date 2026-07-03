from src.utils import log_message
from src.scraper import fetch_mock_flights
from src.processor import clean_data
from src.analytics import run_analysis
from src.visualization import plot_prices, plot_correlation


def main():
    log_message("Starting Flight Price Monitoring System...")

    # Step 1: Fetch (mock for now)
    df = fetch_mock_flights()

    # Step 2: Clean
    df = clean_data(df)

    # Step 3: Analyze
    results = run_analysis(df)
    log_message(f"Analysis Results: {results}")

    # Step 4: Visualize
    plot_prices(df)

    log_message("Pipeline finished successfully.")

if __name__ == "__main__":
    main()
