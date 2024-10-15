from backtester.data_handler import DataHandler
from backtester.backtester import Backtester
from backtester.strategies import Strategy

def main():
    """Example usage of the backtester."""
    symbol = "AAPL"
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    data = DataHandler(
        symbol=symbol, start_date=start_date, end_date=end_date
    ).load_data()

    