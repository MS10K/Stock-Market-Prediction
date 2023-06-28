import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

def local_css():
    st.markdown("""<style>
    .highlight {
  border-radius: 0.4rem;
  color: white;
  padding: 0.5rem;
  margin-bottom: 1rem;
}
.bold {
  padding-left: 1rem;
  font-weight: 700;
}
.blue {
  background-color: rgba(76,114,117,.7);
}
.red {
  background-color: lightblue;
}</style>""", unsafe_allow_html=True)
local_css()

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.wallpapersafari.com/desktop/1024/576/51/90/iRuUAH.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
# App title
st.markdown('''
# Stock Price App

''')
st.write('---')

# Sidebar
st.subheader('Query parameters')
start_date = st.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.date_input("End date", datetime.date(2022, 1, 31))

# Retrieving tickers data
tickerSymbol = st.text_input('Enter Stock Ticker', 'AAPL')

tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker
st.write('---')
# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
# string_sum=" <div> <span class='highlight blue'>"+ string_summary +"</span></div>"
# st.markdown(string_summary)
string_sum = "<div class='highlight blue'>%s</div>" % tickerData.info['longBusinessSummary']
st.markdown(string_sum, unsafe_allow_html=True)

# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)


#st.write('---')
#st.write(tickerData.info)
