import yfinance as yaf
import pandas as pd 

def fetch_stock_data(ticker: str, period: str = "2y") -> pd.DataFrame:
    try:
         stock = yaf.Ticker(ticker) #point yfin to ticker
         df = stock.history(period=period)#pull daily price history, 2y points to past two years of trading days
         df = df[["Close"]] #only care about closing price per day
         df.dropna(inplace=True) #remove rows with data missing due to holidays, etc
         return df #return clean data & closing prices 
    except Exception as e: #to not throw error if ticker invalid
        print(f"cant fetch data for this stock {ticker}: {e}")
        return pd.DataFrame() #return empty df if error occurs


   


