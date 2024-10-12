"""Base class for trading strategies."""

from typing import Any

import pandas as pd

class Strategy:

    def __init__(self, indicators: dict, signal_logic: Any):
        self.indicators = indicators
        self.signal_logic = signal_logic