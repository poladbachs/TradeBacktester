
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
        
