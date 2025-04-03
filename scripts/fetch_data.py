import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    data.to_csv(f"data/{ticker}_stock_data.csv")
    print(f"Saved {ticker} stock data to data/{ticker}_stock_data.csv")

if __name__ == "__main__":
    ticker = "AAPL"  # Change this to any stock symbol
    start_date = "2024-01-01"
    end_date = "2025-01-01"
    fetch_stock_data(ticker, start_date, end_date)
