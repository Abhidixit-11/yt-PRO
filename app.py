import streamlit as st
import google.generativeai as genai
import asyncio

# Ye line add karo taaki loop ki dikkat na ho


genai.configure(api_key=st.secrets["API_KEY"])