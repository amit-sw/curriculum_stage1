import streamlit as st
from db_utils import get_all_curriculums
import pandas as pd

def show_display():
    st.header("Saved Curricula")
    columns, data = get_all_curriculums()
    if not data:
        st.info("No curricula found.")
        return
    df = pd.DataFrame(data, columns=columns)
    # Optional: Show the table nicely
    #st.dataframe(df)
    # Or show individual cards for each entry
    for _, row in df.iterrows():
        with st.expander(f"Topic: {row['topic']}"):
            st.write(f"**Topic Sentence:** {row['topic_sentence']}")
            if pd.notna(row.get('topic_expansion', None)) and row['topic_expansion']:
                st.write(f"**Expansion:** {row['topic_expansion']}")
            if pd.notna(row.get('session_duration', None)) and row['session_duration']:
                st.write(f"**Session Duration (min):** {row['session_duration']}")
            st.divider()
            st.write(f"**Prompt:** {row['prompt']}")
            st.divider()
            st.write(f"**Response:** {row['response']}")
            st.divider()