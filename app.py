import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup
genai.configure(api_key="AQ.Ab8RN6IkIlV3S10-cDuPEkhsSbYaqlYS9QbsXdjgRSajgPFE7w")
model = genai.GenerativeModel('gemini-2.5-flash')

# Page Config
st.set_page_config(page_title="YT Pro AI", page_icon="🤖", layout="centered")
st.title("🤖 YouTube Pro Assistant")

# Sidebar: Image Upload ka option
with st.sidebar:
    st.header("Thumbnail Tools")
    uploaded_file = st.file_uploader("Apni photo upload karo:", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input (Bottom bar)
if prompt := st.chat_input("Type"):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant"):
        # Agar photo upload ki hai toh AI ko context bhejo
        if uploaded_file:
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)
            
        st.markdown(response.text)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})