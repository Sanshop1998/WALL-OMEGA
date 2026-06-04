import streamlit as st
import google.generativeai as genai
import os

# --- 1. KONFIGURASI PRO DAN UI ---
st.set_page_config(
    page_title="WALL OMEGA | AI Engine",
    page_icon="⚡",
    layout="wide"
)

# Styling kustom agar terlihat seperti aplikasi kelas dunia
st.markdown("""
    <style>
    .main { background-color: #0f1117; color: white; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA KEAMANAN & API ---
if "GEMINI_API_KEY" not in st.secrets:
    st.error("⚠️ Sistem API belum terdeteksi. Pastikan Anda mengisi Secrets di Dashboard Streamlit.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- 3. FUNGSI LOGIKA AI (MODULAR) ---
def generate_viral_script(topic, tone, length):
    """Fungsi cerdas untuk menghasilkan konten viral"""
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    Bertindaklah sebagai ahli viral konten media sosial. 
    Buatlah skrip yang sangat memikat untuk topik: {topic}.
    Gunakan gaya bahasa: {tone}.
    Target durasi: {length}.
    Struktur: Hook yang kuat, Body yang informatif, dan Call-to-Action yang menggugah.
    """
    return model.generate_content(prompt).text

# --- 4. TAMPILAN ANTARMUKA (UI) ---
st.title("⚡ WALL OMEGA | AI Viral Engine")
st.markdown("Platform generator konten dengan performa tinggi.")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Konfigurasi")
    topic = st.text_input("Topik Konten:", placeholder="Contoh: Masa depan AI")
    tone = st.selectbox("Gaya Bahasa:", ["🔥 Viral & Hype", "🧠 Edukatif & Mendalam", "🎭 Dramatis & Emosional", "💼 Profesional"])
    length = st.select_slider("Durasi (Detik):", options=[15, 30, 60, 90, 120])
    
    if st.button("Generate Sekarang"):
        if not topic:
            st.warning("Mohon masukkan topik terlebih dahulu!")
        else:
            with st.spinner("Sedang meracik konten viral..."):
                try:
                    result = generate_viral_script(topic, tone, length)
                    st.session_state['output'] = result
                except Exception as e:
                    st.error(f"Error pada Engine AI: {e}")

with col2:
    st.header("Hasil Output")
    if 'output' in st.session_state:
        st.markdown(st.session_state['output'])
    else:
        st.info("Hasil skrip Anda akan muncul di sini setelah klik Generate.")
