import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="WALL OMEGA", layout="centered")

# Mengambil kunci
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key belum diset di Secrets!")
    st.stop()

# Konfigurasi menggunakan model yang paling stabil untuk akun baru
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro') 

st.title("⚡ WALL OMEGA")

topic = st.text_input("Apa topik konten viral Anda?")

if st.button("Generate Skrip"):
    if topic:
        with st.spinner("Sedang memproses..."):
            try:
                response = model.generate_content(f"Buat skrip viral yang menarik tentang: {topic}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Masukkan topik dulu!")
