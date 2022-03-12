import yfinance as yf
#import matplotlib.pyplot as plt
import streamlit as st
st.write("""
#Sample Stock Price app

Shown are the stock price and volume of Google!

""")
ts='GOOGL'
tickerdata = yf.Ticker(ts)
tickerdf= tickerdata.history(period='1d',start='2020-03-01',end='2022-03-01')
st.line_chart(tickerdf.Close)
st.line_chart(tickerdf.Volume)


