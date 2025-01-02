import yfinance as yf
import streamlit as st
from datetime import datetime as dt
import pandas as pd

st.write('# Simple Stock Price App')

# user inputs the ticker symbol of the company they want to see the stock price for
user_input = st.text_input("Enter a Stock Ticker Symbol (e.g: AAPL, GOOGL, NVDA) - ")

# define the ticker symbol
tickerSymbol = user_input

# gets the data (from yahoo finance) for this ticker
tickerData = yf.Ticker(tickerSymbol)

# gets historical prices for the ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=dt.today().strftime('%Y-%m-%d'))

longName = tickerData.info['longName']
st.write(f"## {longName}")

st.write("## Closing Price")
st.line_chart(tickerDf.Close)

st.write("## Volume Price")
volume = st.line_chart(tickerDf.Volume)

