# pages/New_Curriculum.py
import streamlit as st
from config import DEFAULT_PROMPT, TOPIC_PROMPT, DESCRIPTION_PROMPT
from db_utils import insert_curriculum
from llm_utils import get_topic_name, get_curriculum, get_topic_description

def show_new_curriculum():
    st.header("New Curriculum")
    topic_sentence = st.text_input("Topic Sentence (required):")
    topic_name = st.text_input(
        "Topic Name (optional):", value=st.session_state.get("topic_name", "")
    )
    topic_description = st.text_area(
        "Topic Description (optional):",
        value=st.session_state.get("topic_description", ""),
    )
    prompt = st.text_area("Prompt for curriculum:", value=DEFAULT_PROMPT)

    if st.button("Generate Curriculum", disabled=not topic_sentence):
        with st.spinner("Processing..."):
            missing = False
            if not topic_name:
                topic_name = get_topic_name(topic_sentence, TOPIC_PROMPT)
                st.session_state["topic_name"] = topic_name
                missing = True
            if not topic_description:
                topic_description = get_topic_description(
                    topic_sentence, DESCRIPTION_PROMPT
                )
                st.session_state["topic_description"] = topic_description
                missing = True

            if missing:
                st.success(
                    "Missing fields generated. Please review and press the button again to create the curriculum."
                )
                st.write(f"### Topic Name\n{topic_name}")
                st.write(f"### Topic Description\n{topic_description}")
                return

            curriculum = get_curriculum(
                f"{topic_name}\n\n{topic_description}", prompt
            )
            insert_curriculum(topic_sentence, topic_name, prompt, curriculum)
            st.success("Curriculum generated!")
            st.write(f"### Topic Name\n{topic_name}")
            st.write(f"### Topic Description\n{topic_description}")
            st.write(f"### Curriculum\n{curriculum}")