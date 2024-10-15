# Trade Backtester
Custom Backtester for Algorithmic Trading Strategies

## Project Overview

**TradeBacktester** is a Python-based application designed for backtesting algorithmic trading strategies. It allows users to implement and test various strategies using historical data. The project is modular, with separate components for handling data, strategies, and performance evaluation. The backtesting tool provides insights into trading strategy effectiveness by calculating key performance metrics such as total return, Sharpe ratio, Sortino ratio, and maximum drawdown.

## Technologies Used

- **Python** for back-end logic and data processing.
- **OpenBB SDK** for fetching financial data.
- **Pandas** for data manipulation and analysis.
- **NumPy** for performance metric calculations.
- **Matplotlib** for performance visualization and plotting.

## What I Did in This Project

In the **TradeBacktester** project, I implemented:

- **Data Handler Module**:
  - Utilized OpenBB to load historical equity data and processed it using **Pandas**.
  - Created functionality for loading multiple symbols at once and parsing data from CSV files.
  
- **Strategy Module**:
  - Built a base class to handle strategy logic, allowing for dynamic strategy creation with technical indicators.
  - Developed signal generation based on custom logic and applied it to multiple datasets simultaneously.
  
- **Backtester Module**:
  - Simulated trades based on strategy signals, updating the portfolio and calculating positions and total value over time.
  - Integrated commission calculations into each trade to provide more accurate performance results.
  
- **Performance Metrics**:
  - Calculated total return, annualized return, annualized volatility, Sharpe ratio, Sortino ratio, and maximum drawdown.
  - Displayed these metrics in a clear format and visualized them using Matplotlib plots.
  
- **Three Trading Strategies**:
  - Implemented and tested three different trading strategies: SMA Crossover, Mean Reversion, and Pairs Trading.

## Strategy Implementations

### 1. **SMA Crossover Strategy**

The SMA Crossover Strategy involves trading two assets based on the crossover of their 20-day and 60-day simple moving averages (SMA). A buy signal is generated when the short-term SMA (20-day) crosses above the long-term SMA (60-day), and a sell signal is generated when the short-term SMA crosses below the long-term SMA.

```python
# Strategy, indicators and signal logic
strategy = Strategy(
    indicators={
        "sma_20": lambda row: row["close"].rolling(window=20).mean(),
        "sma_60": lambda row: row["close"].rolling(window=60).mean(),
    },
    signal_logic=lambda row: 1 if row["sma_20"] > row["sma_60"] else -1,
)
```

#### Output Values:
- Final Portfolio Value: 11804.58
- Total Return: 18.05%
- Annualized Return: 18.20%
- Annualized Volatility: 13.06%
- Sharpe Ratio: 1.39
- Sortino Ratio: 2.06
- Maximum Drawdown: -12.07%

#### SMA Crossover Strategy Plot:
![crossover_plot](https://github.com/user-attachments/assets/4eb30cbe-f5d9-4be7-9995-5d7a41eacc92)

---

### 2. **Mean Reversion Strategy**

The Mean Reversion Strategy trades based on the idea that asset prices will return to their historical average. A buy signal is triggered when the price falls more than 3 standard deviations below the 50-day simple moving average (SMA), indicating potential undervaluation. A sell signal occurs when the price exceeds 3 standard deviations above the SMA, suggesting potential overvaluation. This strategy aims to profit from price corrections toward the mean.
```python
strategy = Strategy(
    indicators={
        "sma_50": lambda row: row["close"].rolling(window=50).mean(),
        "std_3": lambda row: row["sma_50"].std() * 3,
        "std_3_upper": lambda row: row["sma_50"] + row["std_3"],
        "std_3_lower": lambda row: row["sma_50"] - row["std_3"],
    },
    signal_logic=lambda row: (
        1
        if row["close"] < row["std_3_lower"]
        else -1 if row["close"] > row["std_3_upper"] else 0
    ),
)
```

#### Output Values:
- Final Portfolio Value: 12062.36
- Total Return: 20.62%
- Annualized Return: 20.71%
- Annualized Volatility: 13.12%
- Sharpe Ratio: 1.58
- Sortino Ratio: 1.71
- Maximum Drawdown: -7.19%

#### Mean Reversion Strategy Plot:
![mean_reversion_plot_std_off](https://github.com/user-attachments/assets/97ba1430-a38c-42e3-b174-056e79b2a9ff)

---

### 3. **Pairs Trading Strategy**

The Pairs Trading Strategy involves simultaneously trading two assets: Netflix (NFLX) and Roku (ROKU). A position is taken when one asset's price moves 5% higher than the other, leveraging real-time price discrepancies without relying on historical data. The strategy aims to identify profitable trading opportunities based on current market conditions by buying the lower-performing asset and selling the higher-performing one until their prices converge.
```python
strategy = Strategy(
    indicators={},
    signal_logic=lambda row: (
        1
        if row["close_NFLX"] > row["close_ROKU"] * 1.05
        else -1
        if row["close_NFLX"] < row["close_ROKU"] * 0.95
        else 0
    )
)
```

#### Output Values:
- Final Portfolio Value: 19009.57
- Total Return: 90.10%
- Annualized Return: 43.41%
- Annualized Volatility: 63.61%
- Sharpe Ratio: 0.68
- Sortino Ratio: 1.10
- Maximum Drawdown: -51.65%

#### Pairs Trading Strategy Plot:
![pairs_trade_plot](https://github.com/user-attachments/assets/9ffc1ed0-5a76-4ae1-a901-6719b25cb264)

---

## Performance Metrics

For each backtested strategy, the following performance metrics are calculated:

- **Total Return**: The overall return generated by the strategy.
- **Annualized Return**: The compounded yearly return based on the daily portfolio changes.
- **Annualized Volatility**: The yearly volatility of the strategy's returns.
- **Sharpe Ratio**: A measure of risk-adjusted return, comparing the strategy's return to its volatility.
- **Sortino Ratio**: Similar to the Sharpe ratio, but focuses on downside risk.
- **Maximum Drawdown**: The largest percentage drop from a peak portfolio value to a trough.

## Conclusion

The **TradeBacktester** project provides a robust framework for backtesting trading strategies, calculating key performance metrics, and visualizing strategy effectiveness. By separating data handling, strategy implementation, and performance calculation, the project is highly modular and allows for easy extension to new strategies or data sources.
