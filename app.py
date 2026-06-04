import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="WALL OMEGA", layout="wide")

# Mengambil kunci dengan cara yang lebih aman
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key belum diset! Pergi ke Settings > Secrets di Dashboard Streamlit.")
    st.stop()

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Gagal koneksi ke AI: {e}")
    st.stop()

st.title("🚀 WALL OMEGA | AI Engine")
topic = st.text_input("Masukkan topik konten:")

if st.button("Generate"):
    if topic:
        with st.spinner("Sedang memproses..."):
            try:
                response = model.generate_content(f"Buat skrip viral tentang: {topic}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error AI: {e}")
    else:
        st.warning("Masukkan topik dulu!")
