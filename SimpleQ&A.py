
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os

## Function to load openai model and get response

def get_openai_response(question):
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", 
               temperature=0.5,
               openai_api_key=os.environ['OPENAI_API_KEY'])
    response = llm.invoke(question)
    return response

##Initialize streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application For Q&A")

input = st.text_input("Input: ", key="input")
response=get_openai_response(input)

submit = st.button("Generate Response")

if submit:
    st.subheader("The Response is")
    st.write(response.content)

