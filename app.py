import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="WALL OMEGA", layout="wide")

# Mengambil kunci
api_key = st.secrets.get("GEMINI_API_KEY")

st.title("⚡ WALL OMEGA | AI Engine")

if not api_key:
    st.error("API Key kosong di Secrets! Harap isi di Settings > Secrets.")
else:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        topic = st.text_input("Topik Konten:")
        if st.button("Generate"):
            with st.spinner("Meracik..."):
                response = model.generate_content(f"Buat skrip viral tentang: {topic}")
                st.markdown(response.text)
    except Exception as e:
        st.error(f"Error Koneksi: {e}. Pastikan API Key benar dan masih aktif.")
