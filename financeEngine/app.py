#2 visualize what is happening

import streamlit as st #turn data scripts into interactive web app
import plotly.graph_objects as go # interactive charts, better than matlab because more apt for stock related 
import sys
import os 


#where 2 find data/ & core/ from within dashboard/ 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from data.fetch import fetch_stock_data
from core.indicators import add_indicators
from core.scanner import check_signal

watchlist = [
    "AAPL", "NVDA", "MSFT", "GOOGL", "AMZN",
    "AMD", "AVGO", "SPCX", "ORCL", "TSM", "ASML",
    "CRM", "V", "JPM", "BRK-B", "WMT", "LLY",
    ]

st.title("stock scanner dashboard")#st title creates large header on web app
st.markdown("scan for stocks w/ long term uptrend and oversold in short term")

selected = st.selectbox("select stock: ", watchlist) #dropdown menu to select from predefined list 

df = fetch_stock_data(selected) #fetch data 4 selected 
df = add_indicators(df) #add indicators to data

latest = df.iloc[-1] #grab last row of df, today most recent close
close = latest["Close"]
sma200 = latest["SMA200"]
rsi14 = latest["RSI14"]

above_sma = close > sma200 
oversold = rsi14 <= 35

col1, col2, col3 = st.columns(3) #split page into price, sma, rsi 
col1.metric("Price", f"${close:.2f}")
col2.metric("SMA200", f"${sma200:.2f}")
col3.metric("RSI14", f"{rsi14:.2f}")

if above_sma and oversold:
    st.success("buy signal detected") #green success banner 
else:
    st.warning("no signal") #yellow no signal banner

fig = go.Figure() #build chart

fig.add_trace(go.Scatter( #one trace  = one line, this is closing price 
    x=df.index,
    y=df["Close"],
    name="Close Price",
    line=dict(color="purple", width=1.5)
))

fig.add_trace(go.Scatter( #another trace, for SMA )
    x=df.index,
    y=df["SMA200"],
    name="SMA200",
    line=dict(color="green", width=1.5, dash="dash")
))

fig.update_layout( #final chart layout 
    title=f"{selected} — Price vs SMA200",
    xaxis_title="date",
    yaxis_title="price in $",
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, use_container_width=True)#render chart in browser


