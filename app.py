import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Page Config
st.set_page_config(page_title="YouTube Thumbnail AI", layout="centered")

# API Configuration
genai.configure(api_key=st.secrets["API_KEY"])

st.title("🎨 AI YouTube Thumbnail Generator")

# File Uploader
uploaded_file = st.file_uploader("Apni photo upload karo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Generate Thumbnail"):
        with st.spinner("Gemini thumbnail bana raha hai..."):
            # Model Setup
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Prompting for thumbnail ideas
            response = model.generate_content(["Convert this image into a professional YouTube thumbnail style.", image])
            
            st.success("Thumbnail ready!")
            st.write(response.text) # Yahan thumbnail ka link ya suggestion aayega
            
            # Download Button (Optional)
            buf = io.BytesIO()
            image.save(buf, format='PNG')
            byte_im = buf.getvalue()
            st.download_button(label="Download Thumbnail", data=byte_im, file_name="thumbnail.png", mime="image/png")