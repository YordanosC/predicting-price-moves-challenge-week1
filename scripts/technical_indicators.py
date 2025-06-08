import pandas as pd
import numpy as np
import talib
import matplotlib.pyplot as plt
import yfinance as yf

def load_stock_data(ticker='AAPL', start='2024-01-01', end='2025-05-31'):
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
        df = yf.download(ticker, start=start, end=end, auto_adjust=False)
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
    # Ensure Close is numeric and handle NaNs
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna(subset=['Close'])  # Remove rows with NaN in Close
    close = df['Close'].values  # Convert to NumPy array
    
    # Debugging
    print("Close array shape:", close.shape)
    print("Close array dtype:", close.dtype)
    print("NaN count in Close:", np.isnan(close).sum())
    
    # Check for NaNs
    if np.isnan(close).any():
        raise ValueError("NaNs found in Close array after cleaning")
    
    # Calculate indicators
    df['SMA20'] = talib.SMA(close, timeperiod=20)
    df['RSI'] = talib.RSI(close, timeperiod=14)
    df['MACD'], df['MACD_signal'], _ = talib.MACD(close)
    return df

def plot_indicators(df, ticker):
    """
    Plot stock price and indicators.
    
    Args:
        df (pd.DataFrame): Data with indicators.
        ticker (str): Stock ticker symbol.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='#1f77b4')
    plt.plot(df['Date'], df['SMA20'], label='20-Day SMA', color='#ff7f0e')
    plt.title(f'{ticker} Price and 20-Day SMA', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.savefig(f'../plots/{ticker}_sma.png')
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(df['Date'], df['RSI'], label='RSI', color='#2ca02c')
    plt.axhline(70, color='red', linestyle='--', alpha=0.5)
    plt.axhline(30, color='red', linestyle='--', alpha=0.5)
    plt.title(f'{ticker} RSI', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('RSI', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.savefig(f'../plots/{ticker}_rsi.png')
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(df['Date'], df['MACD'], label='MACD', color='#d62728')
    plt.plot(df['Date'], df['MACD_signal'], label='Signal Line', color='#9467bd')
    plt.title(f'{ticker} MACD', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('MACD', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.savefig(f'../plots/{ticker}_macd.png')
    plt.show()

if __name__ == "__main__":
    df = load_stock_data()
    df = calculate_indicators(df)
    plot_indicators(df, 'AAPL')