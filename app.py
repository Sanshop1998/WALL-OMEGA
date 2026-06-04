import streamlit as st
import google.generativeai as genai

# Konfigurasi halaman
st.set_page_config(page_title="WALL OMEGA", layout="wide")

# Mengambil API Key dari Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key belum diset di menu Secrets!")
    st.stop()

# Tampilan utama
st.title("🚀 WALL OMEGA AI")
topic = st.text_input("Apa topik konten viral Anda?")

if st.button("Generate Skrip"):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"Buat skrip viral yang menarik tentang: {topic}")
        st.markdown(response.text)
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
