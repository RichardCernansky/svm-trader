import matplotlib.pyplot as plt

portfolio_values = long_only_trading(df, svm, gamma=0.1, sG=0.05, sL=0.05, initial_cash=1000)

plt.plot(portfolio_values, label="Portfolio Value")
plt.xlabel("Time")
plt.ylabel("Portfolio Value ($)")
plt.legend()
plt.show()
