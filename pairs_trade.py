from backtester.data_handler import DataHandler
from backtester.backtester import Backtester
from backtester.strategies import Strategy

symbol = "NFLX,ROKU"
start_date = "2023-01-01"

import pandas as pd

data = DataHandler(
    symbol=symbol,
    start_date=start_date,
).load_data()

data = pd.merge(
    data["NFLX"].reset_index(),
    data["ROKU"].reset_index(),
    left_index=True,
    right_index=True,
    suffixes=("_NFLX", "_ROKU"),
)

data = data.rename(columns={"close_ROKU": "close"})
data.head()

strategy = Strategy(
    indicators={
        "day_5_lookback_NFLX": lambda row: row["close_NFLX"].shift(5),
        "day_5_lookback_ROKU": lambda row: row["close"].shift(5),
    },
    signal_logic=lambda row: (
        -1
        if row["close_NFLX"] > row["day_5_lookback_NFLX"] * 1.05
        else 1 if row["close_NFLX"] < row["day_5_lookback_NFLX"] * 0.95 else 0
    ),
)