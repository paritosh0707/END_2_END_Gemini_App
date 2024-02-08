from dotenv import load_dotenv
load_dotenv()   # load  environment variables

import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## function to load Gemini Pro Model and get response

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


##  initialize the streamlit app

st.set_page_config(page_title="Gemini Img App")
st.header("Google Gemini Application")

input = st.text_input("Input: ",key="input")

uploaded_file = st.file_uploader("Choos an image ...", type=['jpg', 'png', 'jpeg'])
image=''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Describe Image")

if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response:")
    st.write(response)