from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
import base64
from PIL import Image
import pandas as pd
from io import StringIO

st.set_page_config(page_title="TechGenius", page_icon='🙂')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


data = base64.b64decode("c2stU2JhTlE0WFFGWVcwSkUzckl3enpUM0JsYmtGSkxBWXJvQzlvTFFTZk5PeEx3ekxl")
decoded_data = data.decode('utf-8')
print(decoded_data)

os.environ["OPENAI_API_KEY"] = decoded_data


st.title("TechGenius")

user_input = st.text_input("Enter your Question here")

if st.button("Submit"):
    st.write("Answer:")
    query = user_input
    input_index = 'index.json'
    index = GPTSimpleVectorIndex.load_from_disk(input_index)
    response = index.query(query, response_mode="compact")
    response_str=str(response)
    st.text_input(response_str)
