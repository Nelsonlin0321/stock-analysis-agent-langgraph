import os
from io import StringIO
import pandas as pd
from src.utils import multi_threading, exponential_retry
from typing import Optional, TypedDict
import yfinance as yf
from tabulate import tabulate


class StockPercentageIncrease(TypedDict):
    symbol: str
    percentage_increased: float


class TopStockData(TypedDict):
    symbol: str
    percentage_increased: float
    sample_data_in_markdown: str
    data_csv_path: str
    pandas_dataframe_info: str


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


def get_top_nasdaq_stock_data(number_of_days: int = 5) -> TopStockData:
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

    symbol = top_nasdaq_performance["symbol"]
    df = fetch_stock_data(
        symbol=symbol, number_of_days=number_of_days)

    sample_data_in_markdown = convert_to_markdown_table(df)
    data_path = f"./data/{symbol}_performance_in_the_past_{number_of_days}_days.csv".lower()
    data_path = os.path.abspath(data_path)
    df.to_csv(data_path, index=False)
    pandas_dataframe_info = capture_df_info(df)

    return {
        'symbol': top_nasdaq_performance["symbol"],
        'percentage_increased': top_nasdaq_performance["percentage_increased"],
        'sample_data_in_markdown': sample_data_in_markdown,
        'data_csv_path': data_path,
        "pandas_dataframe_info": pandas_dataframe_info,
    }


def capture_df_info(df):
    """
    Captures the output of df.info() into a string.

    Parameters:
        df (pandas.DataFrame): The dataframe to capture info from.

    Returns:
        str: The captured info as a string.
    """
    buffer = StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()


def convert_to_markdown_table(dataframe):
    """
    Converts the top 5 rows of a DataFrame to a Markdown table.

    Args:
        dataframe (pd.DataFrame): The DataFrame to convert.

    Returns:
        str: The Markdown table as a string.
    """
    return tabulate(dataframe.head(), headers='keys', tablefmt='pipe', showindex=False)


def fetch_stock_data(symbol: str, number_of_days: int) -> pd.DataFrame:
    """
    Fetch stock data for a given symbol and number of days.

    Args:
        symbol (str): The stock symbol to fetch data for.
        number_of_days (int): The number of days of historical data to fetch.

    Returns:
        pd.DataFrame: A DataFrame containing the stock data.
    """
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=f"{number_of_days}d")
    df.reset_index(inplace=True)
    return df


if __name__ == "__main__":
    top_nasdaq_stock_data = get_top_nasdaq_stock_data()
    print(top_nasdaq_stock_data)
