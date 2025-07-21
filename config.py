# config.py
import streamlit as st
DEFAULT_PROMPT = "Generate a concise curriculum for the following topic."
TOPIC_PROMPT = "Generate a topic name for the following sentence."
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
DB_FILE = "output/curriculum.db"