# pages/Display.py
import streamlit as st
from db_utils import get_all_curriculums

def show():
    st.header("Saved Curricula")
    data = get_all_curriculums()
    if data:
        for row in data:
            st.markdown("---")
            st.write(f"**ID:** {row[0]}")
            st.write(f"**Topic Sentence:** {row[1]}")
            st.write(f"**Topic:** {row[2]}")
            st.write(f"**Prompt:** {row[3]}")
            st.write(f"**Response:** {row[4]}")
    else:
        st.info("No curricula found.")