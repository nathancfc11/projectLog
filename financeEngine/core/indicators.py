import pandas as pd
#ta lib handle all math
from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    sma = SMAIndicator(close=df["Close"], window=200) #take closing price and calc rolling avg over 200 days
    df["SMA200"] = sma.sma_indicator() #add as coulumn to clean df
    rsi = RSIIndicator(close=df["Close"], window=14) #calc RSI looking back 14 days
    df["RSI14"] = rsi.rsi()#add column to df 

    return df

    

