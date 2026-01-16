import yfinance as yf
from crewai.tools import tool

@tool("Get stock price")
def get_stock_price(stock_symbol: str) -> str:
    """
    Fetch the current stock price and daily change for a given stock symbol.

    Args:
        stock_symbol (str): Stock ticker symbol (e.g., AAPL, TSLA)

    Returns:
        str: Stock price, daily change, and percentage change
    """
    stock = yf.Ticker(stock_symbol)
    info = stock.info

    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency", "USD")

    if current_price is None:
        return f"Could not fetch price for {stock_symbol}. Please check the symbol."

    return (
        f"Stock: {stock_symbol.upper()}\n"
        f"Price: {current_price} {currency}\n"
        f"Change: {change} ({round(change_percent, 2)}%)"
    )
