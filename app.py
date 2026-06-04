import streamlit as st
import google.generativeai as genai
import os

# 1. Konfigurasi Halaman (UI/UX)
st.set_page_config(page_title="WALL OMEGA Pro", layout="wide")

# 2. Inisialisasi AI (Gemini)
# Mengambil kunci dari Streamlit Secrets (Aman & Profesional)
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("API Key belum diset di menu Secrets!")
    st.stop()

genai.configure(api_key=api_key)

# 3. Struktur Konten (Modular untuk Pengembangan Masa Depan)
VIRAL_HOOKS = ["Nobody talks about this but...", "I spent years learning this", "Stop doing this if you want success"]

# 4. Tampilan Antarmuka
st.title("🚀 WALL OMEGA AI")
st.subheader("Generator Skrip Viral Kelas Dunia")

user_input = st.text_input("Apa topik skrip Anda?")
if st.button("Generate Skrip"):
    with st.spinner("Sedang memproses kecerdasan..."):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"Buat skrip viral tentang: {user_input}")
        st.markdown(response.text)
