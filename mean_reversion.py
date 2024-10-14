from backtester.data_handler import DataHandler
from backtester.backtester import Backtester
from backtester.strategies import Strategy

symbol = "HE"
start_date = "2022-01-01"
end_date = "2022-12-31"

data = DataHandler(symbol=symbol, start_date=start_date, end_date=end_date).load_data()

strategy = Strategy(
    indicators={
        "sma_50": lambda row: row["close"].rolling(window=50).mean(),
        "std_3": lambda row: row["close"].rolling(window=50).std() * 3,
        "std_3_upper": lambda row: row["sma_50"] + row["std_3"],
        "std_3_lower": lambda row: row["sma_50"] - row["std_3"],
    },
    signal_logic=lambda row: (
        1
        if row["close"] < row["std_lower"]
        else -1 if row["close"] > row["std_upper"] else 0
    ),
)