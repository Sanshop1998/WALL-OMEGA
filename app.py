import streamlit as st
from google import genai
from google.genai import types as genai_types
import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="WALL OMEGA — AI Viral Script Generator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"Get Help": None, "Report a bug": None, "About": "WALL OMEGA — The World's Most Advanced AI Viral Script Generator"},
)

DARK_THEME = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.main-header { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); border-radius: 16px; padding: 2.5rem 2rem; margin-bottom: 1.5rem; text-align: center; border: 1px solid rgba(139, 92, 246, 0.3); box-shadow: 0 0 40px rgba(139, 92, 246, 0.15); }
.main-header h1 { font-family: 'Space Grotesk', sans-serif; font-size: 3rem; font-weight: 900; background: linear-gradient(90deg, #8b5cf6, #ec4899, #f59e0b, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: -1px; margin: 0; }
.main-header p { color: rgba(255,255,255,0.6); font-size: 1rem; margin-top: 0.5rem; letter-spacing: 2px; text-transform: uppercase; }
.feature-card { background: linear-gradient(135deg, rgba(139,92,246,0.1), rgba(236,72,153,0.05)); border: 1px solid rgba(139,92,246,0.25); border-radius: 12px; padding: 1.2rem; margin-bottom: 0.8rem; }
.output-container { background: linear-gradient(135deg, #0f172a, #1e1b4b); border: 1px solid rgba(139,92,246,0.4); border-radius: 16px; padding: 2rem; margin-top: 1rem; }
.tip-box { background: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; border-radius: 0 8px 8px 0; padding: 0.8rem 1rem; margin: 0.5rem 0; font-size: 0.85rem; }
.section-divider { border: none; height: 1px; background: linear-gradient(90deg, transparent, rgba(139,92,246,0.5), transparent); margin: 1.5rem 0; }
.history-item { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 0.7rem; margin-bottom: 0.5rem; font-size: 0.82rem; }
.stButton > button { background: linear-gradient(135deg, #7c3aed, #6d28d9) !important; color: white !important; border: none !important; border-radius: 10px !important; font-weight: 600 !important; box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3) !important; }
</style>
"""
st.markdown(DARK_THEME, unsafe_allow_html=True)

PLATFORMS = {
    "🎵 TikTok": {"style": "hook-heavy, fast-paced, Gen-Z energy", "duration": "15–60 seconds", "format": "Hook (3s) → Problem (5s) → Solution (40s) → CTA (5s)", "tone": "Casual, authentic, relatable"},
    "📺 YouTube": {"style": "story-driven, educational, retention-focused", "duration": "8–20 minutes", "format": "Hook (30s) → Intro (1min) → Main Content → Recap → CTA", "tone": "Engaging, authoritative, warm"},
    "📸 Instagram Reels": {"style": "visually descriptive, aesthetic, aspirational", "duration": "15–90 seconds", "format": "Visual hook → Key message → CTA overlay", "tone": "Aspirational, stylish, concise"},
    "💼 LinkedIn": {"style": "professional storytelling, thought leadership", "duration": "3–5 minutes", "format": "Hook story → Insight → Data/Proof → Takeaway → CTA", "tone": "Professional, insightful, credible"},
    "🎙️ Podcast": {"style": "conversational, narrative, deep-dive", "duration": "20–60 minutes", "format": "Intro → Topic Intro → Deep Dive → Insights → Outro", "tone": "Natural, curious, engaging"},
    "🛒 Sales Video": {"style": "persuasion-focused, benefit-driven, urgency-built", "duration": "2–5 minutes", "format": "Pain Point → Agitation → Solution → Benefits → Social Proof → CTA", "tone": "Confident, empathetic, compelling"},
    "📱 Twitter/X Thread": {"style": "punchy, hook-based, knowledge-sharing", "duration": "Read: 3–5 minutes", "format": "Hook tweet → 10-15 value tweets → CTA tweet", "tone": "Confident, witty, sharp"},
    "🎬 YouTube Shorts": {"style": "ultra-fast, viral loop, satisfying", "duration": "15–60 seconds", "format": "Instant Hook → Value Drop → Loop/CTA", "tone": "Energetic, surprising, addictive"},
}

SCRIPT_STYLES = ["🔥 Ultra Viral Hook Style", "📖 Storytelling Narrative", "🎭 Dramatic Reveal", "💡 Educational Breakdown", "😂 Humor & Entertainment", "😤 Controversy & Opinion", "🤯 Mind-Blowing Facts", "💰 AIDA Sales Formula", "🔢 Listicle Format", "❓ Question-Driven", "📊 Data-Backed Authority", "🌊 Emotional Journey"]

NICHE_CATEGORIES = {
    "💰 Business & Finance": ["Entrepreneurship", "Investing", "Side Hustles", "Marketing", "E-commerce", "Crypto", "Real Estate"],
    "🏋️ Health & Fitness": ["Gym & Workout", "Weight Loss", "Mental Health", "Nutrition", "Biohacking", "Yoga"],
    "🎮 Entertainment": ["Gaming", "Movies & TV", "Music", "Comedy", "Anime", "Sports"],
    "🛠️ Tech & AI": ["Artificial Intelligence", "Software Dev", "Gadgets", "Cybersecurity", "Apps & Tools", "Web3"],
    "✈️ Travel & Lifestyle": ["Travel Vlogs", "Luxury Lifestyle", "Budget Travel", "Food & Cuisine", "Fashion"],
    "📚 Education": ["Science", "History", "Philosophy", "Languages", "Self-Help", "Psychology"],
    "💄 Beauty & Fashion": ["Makeup", "Skincare", "Fashion Trends", "Haul Videos", "Transformation"],
    "🏠 Home & DIY": ["Interior Design", "DIY Projects", "Cooking & Recipes", "Gardening", "Organization"],
}

VIRAL_HOOKS = ["Nobody talks about this but...", "I spent [X] years learning what I'm about to tell you in [Y] minutes...", "Stop doing [X] if
