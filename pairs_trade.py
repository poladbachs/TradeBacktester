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