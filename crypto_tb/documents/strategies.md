# Crypto trading strategies

## Market Making
How It Works: The bot places both buy and sell limit orders to profit from the bid-ask spread.
Best for: Stable market conditions with high liquidity.
Example: If BTC/USDT is 50,000, the bot places:
A buy order at 49,950.
A sell order at 50,050.
If both execute, the bot earns a 100 profit per BTC.
✅ Pros:

Generates consistent profits in liquid markets.
Works well with large capital.
❌ Cons:

Requires high-frequency trading (HFT) and low fees.
Can be risky during high volatility.

## Arbitrage Trading
How It Works: Exploits price differences between exchanges or trading pairs.
Best for: Traders who can quickly execute trades across multiple exchanges.
📌 Types of Arbitrage:

Spatial Arbitrage – Buying on Binance (BTC = 50,000) and selling on Kraken (BTC = 50,500).
Triangular Arbitrage – Trading between three pairs on the same exchange, e.g.:
Convert BTC → ETH.
Convert ETH → USDT.
Convert USDT → BTC, profiting from small price mismatches.
✅ Pros:

Low risk, since you profit from price differences.
Does not depend on market trends.
❌ Cons:

Slow execution can kill profits (prices change fast).
Requires low fees & fast API access.

## Trend Following (Momentum Trading)
How It Works: The bot buys when prices are rising and sells when prices fall, following market trends.
Best for: Medium to long-term traders.
📌 Common Indicators Used:

Moving Averages (SMA, EMA) → Identify price trends.
MACD (Moving Average Convergence Divergence) → Detects momentum shifts.
RSI (Relative Strength Index) → Measures overbought/oversold conditions.
✅ Pros:

Simple and effective for bull markets.
Can be used with machine learning models.
❌ Cons:

Lags during sideways (choppy) markets.
Can lead to false signals.
## Mean Reversion (Reversal Trading)
How It Works: Assumes prices always return to their average (mean) after a big move.
Best for: Trading volatile markets.
📌 Common Indicators Used:

Bollinger Bands – Buy when price hits the lower band; sell when it reaches the upper band.
RSI (Relative Strength Index) – Buy when oversold (below 30), sell when overbought (above 70).
✅ Pros:

Profitable in sideways markets.
Works well with highly volatile assets.
❌ Cons:

Can be risky in strong trends (a crashing price might not bounce back).

## Scalping (High-Frequency Trading)
How It Works: The bot makes small, frequent trades to take advantage of tiny price movements.
Best for: Traders who want to make quick profits multiple times per day.
📌 Example:

Buy BTC at 50,000 → Sell at 50,050 (profit = 50).
Do this 100 times per day for small but steady profits.
✅ Pros:

Generates quick and small profits frequently.
Works well with high leverage.
❌ Cons:

Requires very low fees & high-speed execution.
Risky if market moves too fast.

## Grid Trading
How It Works: Places buy and sell orders at predefined price levels in a grid pattern.
Best for: Sideways or ranging markets.
📌 Example: If BTC is $50,000:

The bot places buy orders at 49,500, 49,000, 48,500.
The bot places sell orders at 50,500, 51,000, 51,500.
Profits from price fluctuations.
✅ Pros:

Profitable even in non-trending markets.
Works best in high volatility.
❌ Cons:

Capital-intensive (requires holding multiple positions).
Ineffective in strong trends.
