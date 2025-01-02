import yfinance as yf
import streamlit as st
from datetime import datetime as dt
import pandas as pd

st.write('Simple Stock Price App')

user_input = st.text_input("Enter a Stock Ticker Symbol (e.g: AAPL, GOOGL, NVDA) - ")

tickerSymbol = user_input

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end=dt.today().strftime('%Y-%m-%d'))

st.write(tickerData.info['longName'])

st.line_chart(tickerDf.Close)
volume = st.line_chart(tickerDf.Volume)


