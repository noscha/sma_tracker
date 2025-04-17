from enum import Enum

import yfinance as yf
import datetime
import pytz

# Define stock ticker and parameters
class Tickers(Enum):

    sp500 = "^GSPC", "200d", "S&P500"
    ndx100 = "^NDX", "220d", "Nasdaq100"
    # tB10 = "BNSXFTYU", "50d", "10year bonds"
    tB20 = "^IDCT20RT", "60d", "20year bonds"


# checks if stock exchange open
def check_time():

    nyc_tz = pytz.timezone('America/New_York')
    nyc_datetime = datetime.datetime.now(nyc_tz)
    current_time = nyc_datetime.time()

    # Define market hours as time objects
    market_open = datetime.time(9, 30)
    market_close = datetime.time(16, 0)

    if market_open < market_close:
        return market_open <= current_time <= market_close
        # Handle overnight periods (not needed for standard market hours)
    else:
        return current_time >= market_open or current_time <= market_close


# Function to fetch historical stock data
def fetch_stock_data(ticker, period):

    stock = yf.Ticker(ticker)
    data = stock.history(period=period)

    # CHECK len data, and NaN

    if ticker == "^IDCT20RT":
        print(data)
    return data

# Function to calculate SMA
def calculate_sma_to_index(data):

    sma = round(data.loc[:, 'Close'].mean(), 2)
    last_close = round(data['Close'].iloc[-1], 2)
    deviation_in_percent = round((last_close - sma) / sma * 100, 2)

    return sma, last_close, deviation_in_percent


if __name__ == "__main__":

    if not check_time():
        print("Market might be open, check for holidays")

    for entry in Tickers:
        *entry, name = entry.value
        data = fetch_stock_data(*entry)
        sma, last_close, deviation_in_percent = calculate_sma_to_index(data)

        print(f"{name}, has SMA of {sma}, last close of {last_close} and deviation of {deviation_in_percent}")

        # TOD0 above 200 for buy, under for sell