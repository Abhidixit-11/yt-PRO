import streamlit as st
import google.generativeai as genai

# API key configure karo
# Laptop par chalane ke liye (Ise baad mein hata dena)
import os
os.environ["API_KEY"] = "AQ.Ab8RN6IkIlV3S10-cDuPEkhsSbYaqLYS9QbsXdjgRSajgPFE7w"
genai.configure(api_key=os.environ["API_KEY"])

# Kuch display karne ke liye likho
st.title("Gemini AI App")
user_input = st.text_input("Kuch pucho:")

if user_input:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    st.write(response.text)