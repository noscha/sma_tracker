import yfinance as yf

# Function to fetch historical stock data
def fetch_stock_data(ticker, period):

    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

# Function to calculate SMA
def calculate_sma_to_index(data):

    sma = round(data.loc[:, 'Close'].mean(), 2)
    last_close = round(data['Close'].iloc[-1], 2)
    deviation_in_percent = round((last_close - sma) / sma * 100, 2)

    return sma, last_close, deviation_in_percent


if __name__ == "__main__":
    # Define stock ticker and parameters

    sp500 = "^GSPC", "200d"
    ndx100 = "^NDX", "220d"
    #tB10 = "BNSXFTYU", "50d"
    tB20 = "^IDCT20RT", "60d"
