#from data.fetch import fetch_stock_data

#df = fetch_stock_data("AAPL") #fetch from clean df 
#print("raw prices for chosen stock: ")
#print(df)

#important context about outputs
# US markets close at 4pm EST, which is 9pm british
#so depending on the time of day this code is executed, THE LATEST VALUE IS what the live price is
#its imperative its run after markets have closed 

from data.fetch import fetch_stock_data
from core.indicators import add_indicators
from core.scanner import check_signal

#testing 
#df = fetch_stock_data("AAPL") 
#df = add_indicators(df) #add indicators to clean df
#print(df.tail(10))

#switch this to tier system eventually, in sticky notes > trading212 strat
watchlist = [
    "AAPL", "NVDA", "MSFT", "GOOGL", "AMZN",
    "AMD", "AVGO", "ORCL", "TSM", "ASML",
    "CRM", "V", "JPM", "BRK-B", "WMT", "LLY",
    ]

for ticker in watchlist:
    df = fetch_stock_data(ticker) #data for each ticker
    df = add_indicators(df) #add indicators to each ticker data
    check_signal(df, ticker) #check buy signal for each ticker 



