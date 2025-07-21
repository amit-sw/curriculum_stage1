# pages/Modify_Curriculum.py
import streamlit as st
from db_utils import (
    get_all_topics,
    get_curriculum_by_topic,
    update_curriculum,
    update_response,
)
from llm_utils import get_curriculum


def show_modify_curriculum():
    c1,c2= st.columns(2)
    c1.header("Modify Curriculum")

    topics = [t[1] for t in get_all_topics()]
    if not topics:
        st.info("No curricula found.")
        return

    selected_topic = c2.selectbox("Select Topic", topics)
    data = get_curriculum_by_topic(selected_topic)
    if not data:
        st.error("Topic not found.")
        return

    st.divider()
    topic_sentence = st.text_input("Topic Sentence", value=data["topic_sentence"])
    topic = st.text_input("Topic", value=data["topic"])
    prompt = st.text_area("Prompt", value=data["prompt"])
    topic_expansion = st.text_area("Topic Expansion (optional):", value=data.get("topic_expansion") or "")
    session_duration = st.number_input("Session Duration (minutes, optional):", min_value=0, value=int(data.get("session_duration") or 0), step=5)
    st.divider()
    st.text_area("Response", value=data["response"], disabled=True, height=200)

    col1, col2 = st.columns(2)
    if col1.button("Save"):
        update_curriculum(
            data["id"],
            topic_sentence,
            topic,
            prompt,
            topic_expansion or None,
            float(session_duration) if session_duration > 0 else None,
        )
        st.success("Saved")
    if col2.button("Generate"):
        with st.spinner("Generating..."):
            response = get_curriculum(prompt,topic_sentence, topic_expansion, session_duration)
            update_response(data["id"], response)
            st.session_state["generated_response"] = response
            st.success("Response updated")
            st.text_area(
                "Response",
                value=response,
                disabled=True,
                height=200,
                key="updated_response",
            )
