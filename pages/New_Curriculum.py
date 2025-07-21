# pages/New_Curriculum.py
import streamlit as st
from config import DEFAULT_PROMPT, TOPIC_PROMPT
from db_utils import insert_curriculum
from llm_utils import get_topic_name, get_curriculum

def show():
    st.header("New Curriculum")
    topic_sentence = st.text_input("Enter a topic sentence:")
    prompt = st.text_area("Prompt for curriculum:", value=DEFAULT_PROMPT)
    if st.button("Generate Curriculum", disabled=not topic_sentence):
        with st.spinner("Generating..."):
            topic = get_topic_name(topic_sentence, TOPIC_PROMPT)
            curriculum = get_curriculum(topic, prompt)
            insert_curriculum(topic_sentence, topic, prompt, curriculum)
            st.success("Curriculum generated!")
            st.write(f"### Topic Name\n{topic}")
            st.write(f"### Curriculum\n{curriculum}")