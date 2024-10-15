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

    strategy = Strategy(
        indicators={
            "sma_20": lambda row: row["close"].rolling(window=20).mean(),
            "sma_60": lambda row: row["close"].rolling(window=60).mean(),
        },
        signal_logic=lambda row: 1 if row["sma_20"] > row["sma_60"] else -1,
    )

    data = Strategy.generate_signals(data)