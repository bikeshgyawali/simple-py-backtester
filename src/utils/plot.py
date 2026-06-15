import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def plot_performance(portfolio_history, market_prices, initial_portfolio, final_portfolio):
    strategy_growth = [val / portfolio_history[0] * 100 for val in portfolio_history]
    market_growth = [val / market_prices[0] * 100 for val in market_prices]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(strategy_growth, label="My Strategy", color="blue", linewidth=2)
    plt.plot(market_growth, label="Market Benchmark (SPY)", color="orange", linestyle="--")
    plt.title("Strategy vs Market Performance (Normalized to 100)", fontsize=14, fontweight="bold")
    plt.xlabel("Trading Days", fontsize=12)
    plt.ylabel("Growth (%)", fontsize=12)
    plt.legend(fontsize=11)
    plt.gca().text(0.02, 0.76, f"Initial Portfolio: ${initial_portfolio:,.2f}\nFinal Portfolio:   ${final_portfolio:,.2f}", transform=plt.gca().transAxes, fontsize=10, fontfamily="monospace", verticalalignment="top", bbox=dict(boxstyle="round,pad=0.6", facecolor="white", edgecolor="none"))
    plt.grid(True, linestyle=":", alpha=0.6)
    
    plt.tight_layout()
    plt.show()