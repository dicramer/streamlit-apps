import google.generativeai as genai
import streamlit as st # Falls du die Secrets von Streamlit nutzt

# Konfigurieren
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Alle Modelle auflisten, die Text generieren können
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
