import streamlit as st
import google.generativeai as genai

# Setup Halaman
st.set_page_config(page_title="WALL OMEGA | Pro", layout="wide")

# Mengambil API Key dari Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key belum diset! Masukkan di Settings > Secrets.")
    st.stop()

# Konfigurasi AI
genai.configure(api_key=api_key)
# Menggunakan model flash yang super cepat dan sangat cerdas untuk konten viral
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Kamu adalah pakar konten viral kelas dunia. Tugasmu adalah membuat skrip yang hook-nya mematikan, retensinya tinggi, dan bahasanya persuasif. Selalu gunakan format yang rapi (poin-poin, emoji secukupnya, dan CTA yang kuat)."
)

# UI Keren
st.title("⚡ WALL OMEGA | AI Engine")
st.subheader("Dominasi Algoritma dengan Konten Berbasis AI")

col1, col2 = st.columns([1, 2])

with col1:
    topic = st.text_input("Topik Utama:")
    platform = st.selectbox("Platform Target:", ["TikTok", "Instagram Reels", "YouTube Shorts", "Twitter/X Thread"])
    tone = st.select_slider("Tone Suara:", options=["Formal", "Edukatif", "Provokatif", "Santai/Gokil"])
    btn = st.button("🚀 Generate Konten Viral")

with col2:
    if btn:
        if topic:
            with st.spinner("Sedang meracik konten tingkat dewa..."):
                try:
                    prompt = f"Buat skrip {platform} dengan tone {tone} untuk topik: {topic}. Pastikan ada Hook di 3 detik pertama, isi yang padat, dan Call to Action di akhir."
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.markdown(response.text)
                    st.success("Konten berhasil diracik!")
                except Exception as e:
                    st.error(f"Gagal generate: {e}")
        else:
            st.warning("Masukkan topik terlebih dahulu, Founder!")
