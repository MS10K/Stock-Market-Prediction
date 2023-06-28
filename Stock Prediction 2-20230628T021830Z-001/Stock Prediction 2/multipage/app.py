import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
	page_title="Main Menu",
	page_icon="✌",

)


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

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

def text_box_highlight(val):
	mark = "<div class='highlight blue'>%s</div>" % val
	st.markdown(mark, unsafe_allow_html=True)

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




st.title("Main Page")
st.sidebar.success("Select a page above.")
url = "https://derick1603-stockss-app-8b7qas.streamlitapp.com/"
st.write("[For Prediction](%s)" % url)
st.write('---')

lottie_coding = load_lottiefile("pages/1lottie.json")

info = 'Investing in the stock market is one of the most complicated and sophisticated ways to conduct business. The stock market is very uncertain since stock values fluctuate due to a variety of factors, making stock prediction a difficult and exceedingly hard task. Investors nowadays require rapid and reliable information to make efficient judgments, with rapidly expanding technology breakthroughs in stock price prediction. This has attracted their interest in the research area. Understanding the pattern of stock price of a particular company and predicting their future development and financial growth will be highly beneficial. This paper focuses on the usage of a type of RNN(recurrent neural network) based Machine learning which is known as Long Short-Term Memory (LSTM) to predict stock values'

lotti_coding = load_lottiefile("pages/1lottie.json")
text_box_highlight(info)
st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    # medium ; high
     # canvas
    height=None,
    width=None,
    key=None,
)