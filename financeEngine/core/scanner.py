def check_signal(df, ticker):

    if df.empty: #error handling 
        print(f"No data for {ticker}, skipping signal check.")
        return 
    
    latest = df.iloc[-1] #grab last row of df, today's most recent close

    close = latest["Close"]
    sma200 = latest["SMA200"]
    rsi14 = latest["RSI14"]

    above_sma = close > sma200 #boolean 4 todays price over 200 day sma (average)
    oversold = rsi14 <= 35 #is tsi beaten down enuf

    if above_sma and oversold: #print buy signal if both are true 
        print(f"BUY SIGNAL: {ticker}")
        print(f"price: $ {close:.2f}")
        print(f"SMA200: $ {sma200:.2f}")
        print(f"RSI14: {rsi14:.2f}")
    else: #obvious 
        print (f"NO SIGNAL: {ticker}")
        print(f"price: $ {close:.2f}")  
        print(f"SMA200: $ {sma200:.2f}")
        print(f"RSI14: {rsi14:.2f}")