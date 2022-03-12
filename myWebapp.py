import yfinance as yf
#import matplotlib.pyplot as plt
import streamlit as st
st.write ("""
#srinivas
asadfsk
""")

ts='MSFT'
tickerdata = yf.Ticker(ts)
tickerdf= tickerdata.history(period='1d',start='2022-03-01',end='2022-03-10')
data=tickerdf.Close
data
