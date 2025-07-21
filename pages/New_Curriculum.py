import streamlit as st
from config import DEFAULT_PROMPT, TOPIC_PROMPT
from db_utils import insert_curriculum
from llm_utils import get_topic_name, get_curriculum  # or openai_utils if that's your file

def show_new_curriculum():
    st.header("New Curriculum")
    topic_sentence = st.text_input("Enter a topic sentence:")
    prompt = st.text_area("Prompt for curriculum:", value=DEFAULT_PROMPT)
    topic_expansion = st.text_area("Topic expansion (optional):", value="", help="Extra notes, scope, or clarification (optional)")
    session_duration = st.number_input("Session duration (minutes, optional):", min_value=0, value=0, step=5, help="Approximate length of session")
    if st.button("Generate Curriculum", disabled=not topic_sentence):
        with st.spinner("Generating..."):
            topic = get_topic_name(topic_sentence, TOPIC_PROMPT)
            curriculum = get_curriculum(prompt,topic_sentence, topic_expansion, session_duration)
            # Convert empty strings and zeros to None
            expansion_value = topic_expansion if topic_expansion.strip() else None
            duration_value = float(session_duration) if session_duration > 0 else None
            insert_curriculum(topic_sentence, topic, prompt, curriculum, topic_expansion=expansion_value, session_duration=duration_value)
            st.success("Curriculum generated and saved!")
            st.write(f"### Topic Name\n{topic}")
            st.write(f"### Curriculum\n{curriculum}")
            if expansion_value:
                st.write(f"**Expansion:** {expansion_value}")
            if duration_value:
                st.write(f"**Session duration:** {duration_value} min")