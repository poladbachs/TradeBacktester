
from typing import List, Dict

import pandas as pd
import matplotlib.pyplot as plt

class Backtester:
    """Backtester class for backtesting trading strategies."""
    def __init__(
        self,
        initial_capital: float = 10000.0,
        commission_pct: float = 0.001,
        commission_fixed: float = 1.0,
    ):
        """Initialize the backtester with initial capital and commission fees."""
        self.initial_capital: float = initial_capital
        self.commission_pct: float = commission_pct
        self.commission_fixed: float = commission_fixed
        self.assets_data: Dict = {}
        self.portfolio_history: Dict = {}
        self.daily_portfolio_values: List[float] = []

    def calculate_commission(self, trade_value: float) -> float:
        """Calculate the commission fee for a trade."""
        return max(trade_value * self.commission_pct, self.commission_fixed)
        
    def execute_trade(self, asset: str, signal: int, price: float) -> None:
        """Execute a trade based on the signal and price."""
        if signal > 0 and self.assets_data[asset]["cash"] > 0:
            trade_value = self.assets_data[asset]["cash"]
            commission = self.calculate_commission(trade_value)
            shares_to_buy = (trade_value - commission) / price
            self.assets_data[asset]["positions"] += shares_to_buy
            self.assets_data[asset]["cash"] -= trade_value
        elif signal < 0 and self.assets_data[asset]["positions"] > 0:
            trade_value = self.assets_data[asset]["positions"] * price
            commission = self.calculate_commission(trade_value)
            self.assets_data[asset]["cash"] += trade_value - commission
            self.assets_data[asset]["positions"] = 0
        
    def update_portfolio(self, asset: str, price: float) -> None:
        """Update the portfolio with the latest price."""
        self.assets_data[asset]["position_value"] = (
            self.assets_data[asset]["positions"] * price
        )
        
