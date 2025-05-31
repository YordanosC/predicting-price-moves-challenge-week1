import pandas as pd
import talib
import matplotlib.pyplot as plt
import yfinance as yf

def load_stock_data(ticker='AAPL', start='2024-01-01', end='2025-05-30'):
    """
    Fetch stock price data using yfinance.
    
    Args:
        ticker (str): Stock ticker symbol.
        start (str): Start date (YYYY-MM-DD).
        end (str): End date (YYYY-MM-DD).
    
    Returns:
        pd.DataFrame: Stock price data.
    """
    try:
        df = yf.download(ticker, start=start, end=end)
        df.reset_index(inplace=True)
        df['Stock'] = ticker
        return df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Stock']]
    except Exception as e:
        raise Exception(f"Error fetching data: {str(e)}")

def calculate_indicators(df):
    """
    Calculate technical indicators using TA-Lib.
    
    Args:
        df (pd.DataFrame): Stock price data.
    
    Returns:
        pd.DataFrame: Data with indicators.
    """
    df['SMA20'] = talib.SMA(df['Close'], timeperiod=20)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    return df

def plot_indicators(df, ticker):
    """
    Plot stock price and indicators.
    
    Args:
        df (pd.DataFrame): Data with indicators.
        ticker (str): Stock ticker symbol.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], df['SMA20'], label='20-Day SMA')
    plt.title(f'{ticker} Price and SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig(f'../plots/{ticker}_sma.png')
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(df['Date'], df['RSI'], label='RSI')
    plt.title(f'{ticker} RSI')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.savefig(f'../plots/{ticker}_rsi.png')
    plt.show()

if __name__ == "__main__":
    df = load_stock_data()
    df = calculate_indicators(df)
    plot_indicators(df, 'AAPL')