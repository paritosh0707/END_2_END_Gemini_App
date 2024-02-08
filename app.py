from dotenv import load_dotenv
load_dotenv()   # load  environment variables

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## function to load Gemini Pro Model and get response

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


##  initialize the streamlit app

st.set_page_config(page_title="Q&A App")
st.header("Google Gemini Application")

input = st.text_input("Input: ",key="input")
submit = st.button("Ask the question...")

##  When submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response:")
    st.write(response)