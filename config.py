# config.py
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
DEFAULT_PROMPT = "Generate a concise curriculum for the following topic."
TOPIC_PROMPT = "Generate a topic name for the following sentence."
DESCRIPTION_PROMPT = "Generate a short description for the following topic sentence."
OPENAI_API_KEY = st.secrets.get('OPENAI_API_KEY', os.environ.get('OPENAI_API_KEY'))
DB_FILE = "output/curriculum.db"