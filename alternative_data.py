from backtester.data_handler import DataHandler
from backtester.backtester import Backtester
from backtester.strategies import Strategy

data = DataHandler(symbol="HE").load_data_from_csv("example_data.csv")
data.head()

strategy = Strategy(
    indicators={},
    signal_logic=lambda row: (1 if row["trade_signal_sentiment"] > 0 else -1),
)
data = strategy.generate_signals(data)

backtester = Backtester()
backtester.backtest(data)
backtester.calculate_performance()