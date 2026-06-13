import streamlit as st
import google.generativeai as genai
import asyncio

# Ye line add karo taaki loop ki dikkat na ho
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

genai.configure(api_key=st.secrets["API_KEY"])