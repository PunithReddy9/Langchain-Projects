# Q&A Chatbot
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os


## Function to load OpenAI model and get response

def get_openai_response(question):
    llm=OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response=llm(question)
    return response

##initializing our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Q&A Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)


