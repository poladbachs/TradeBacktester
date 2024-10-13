"""Performance module for calculating performance metrics."""

import numpy

def calculate_total_return(final_portfolio_value, initial_capital):
    """Calculate the total return of the portfolio."""
    return (final_portfolio_value / initial_capital) - 1

def calculate_annualized_return(total_return, num_days):
    """Calculate the annualized return of the portfolio."""
    return np.power((1 + total_return), 252 / num_days) - 1

def calculate_annualized_volatility(daily_returns):
    """Calculate the annualized volatility of the portfolio."""
    return daily_returns.std() * np.sqrt(252)