import pandas as pd
from src.utils import multi_threading, exponential_retry
from typing import Optional, TypedDict
import yfinance as yf
from loguru import logger


class StockPercentageIncrease(TypedDict):
    symbol: str
    percentage_increased: float
    company_name: Optional[str] = None


@exponential_retry(retries=3)
def fetch_stock_percentage_increase(symbol) -> Optional[StockPercentageIncrease]:
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    if not data.empty:
        open_price = data['Open'].iloc[0]
        close_price = data['Close'].iloc[0]
        percentage_increase = (
            (close_price - open_price) / open_price) * 100
        return {"symbol": symbol, "percentage_increased": float(percentage_increase)}


def get_top_nasdaq_performance_stock() -> StockPercentageIncrease:
    """Get the top performance stock."""

    # with open('./data/nasdaq_data.json', 'r') as f:
    #     nasdaq_data = json.load(f)
    df = pd.read_csv("data/Nasdaq-100.csv")
    nasdaq_stock_symbols = df['Ticker'].tolist()
    stock_percentage_increase_list = multi_threading(function=fetch_stock_percentage_increase,
                                                     parameters=nasdaq_stock_symbols)
    stock_percentage_increase_list = [
        i for i in stock_percentage_increase_list if i]

    top_nasdaq_performance = max(
        stock_percentage_increase_list, key=lambda x: x["percentage_increased"])

    company_name = df[df['Ticker'] ==
                      top_nasdaq_performance["symbol"]].iloc[0].Company

    top_nasdaq_performance['company_name'] = company_name

    logger.info(
        f'Top performance stock: {top_nasdaq_performance}')

    return top_nasdaq_performance


if __name__ == "__main__":
    top_nasdaq_performance_stock = get_top_nasdaq_performance_stock()
    print(top_nasdaq_performance_stock)
