import streamlit as st
from transformers import pipeline

st.title("Hugging Face Demo")
text = st.text_input("Enter text to analyze")
model = pipeline("sentiment-analysis")
if text:
    result = model(text)
    st.write("Sentiment:", result[0]["label"])
    st.write("Confidence:", result[0]["score"])

import google.generativeai as genai

st.title("Gemini Version")
analyze_button = st.button("Analyze Text")

# API Key aus den Streamlit Secrets laden und konfigurieren
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

if analyze_button:
    # Das Gemini-Modell initialisieren und die Systemanweisung übergeben
    model = genai.GenerativeModel(
        model_name="gemini-flash-latest",
        system_instruction="""You are a helpful sentiment analysis assistant.
            You always respond with the sentiment of the text you are given and the confidence of your sentiment analysis with a number between 0 and 1"""
    )
    
    # Text zur Analyse an das Modell schicken
    response = model.generate_content(
        f"Sentiment analysis of the following text: {text}"
    )
    
    # Die Antwort des Modells ausgeben
    st.write(f"The sentiment of the text {text} is {response.text}")



