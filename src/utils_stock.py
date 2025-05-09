import json
import random
from src.utils import multi_threading, exponential_retry
from typing import Optional
from src.types import SymbolWithIncreasePercentage
import yfinance as yf
from loguru import logger


@exponential_retry(retries=3)
def fetch_stock_percentage_increase(symbol) -> Optional[SymbolWithIncreasePercentage]:
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    if not data.empty:
        open_price = data['Open'].iloc[0]
        close_price = data['Close'].iloc[0]
        percentage_increase = (
            (close_price - open_price) / open_price) * 100
        return SymbolWithIncreasePercentage(symbol=symbol, percentage=float(percentage_increase))


def get_top_nasdaq_performance_stock() -> SymbolWithIncreasePercentage:
    """Get the top performance stock."""

    with open('./data/nasdaq_data.json', 'r') as f:
        nasdaq_data = json.load(f)
    nasdaq_data = random.sample(nasdaq_data, 100)  # Simulate a large dataset
    nasdaq_stock_symbols = [stock['Symbol'] for stock in nasdaq_data]
    stock_percentage_increase_list = multi_threading(function=fetch_stock_percentage_increase,
                                                     parameters=nasdaq_stock_symbols)
    stock_percentage_increase_list = [
        i for i in stock_percentage_increase_list if i]

    top_stock_with_increased_percentage = max(
        stock_percentage_increase_list, key=lambda x: x.percentage)
    logger.info(
        f'Top performance stock: {top_stock_with_increased_percentage}')

    return top_stock_with_increased_percentage


if __name__ == "__main__":
    top_nasdaq_performance_stock = get_top_nasdaq_performance_stock()
    print(
        f"Top NASDAQ performance stock: {top_nasdaq_performance_stock.symbol} with percentage increase: {top_nasdaq_performance_stock.percentage}")
    # python -m src.utils_stock
