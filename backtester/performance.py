"""Performance module for calculating performance metrics."""

import numpy

def calculate_total_return(final_portfolio_value, initial_capital):
    """Calculate the total return of the portfolio."""
    return (final_portfolio_value / initial_capital) - 1

