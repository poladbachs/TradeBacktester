
from typing import Optional

import pandas as pd
from openbb import obb

class DataHandler:
    """Data handler class for loading and processing data."""
    def __init__(
        self,
        symbol: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        provider: str = "fmp",
    ):
        self.symbol = symbol.upper()
        self.start_date = start_date
        self.end_date = end_date
        self.provider = provider
