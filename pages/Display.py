# pages/Display.py
import streamlit as st
import pandas as pd
from db_utils import get_all_curriculums

def show_display():
    st.header("Saved Curricula")
    columns,data = get_all_curriculums()
    if not data:
        st.info("No curricula found.")
        return

    #df = pd.DataFrame(data, columns=["ID", "Topic Sentence", "Topic", "Prompt", "Response"])
    df=pd.DataFrame(data, columns=columns)
    #st.table(df)
    topics = df["topic"].unique()

    for topic in topics:
        with st.expander(topic):
            topic_df = df[df["topic"] == topic].reset_index(drop=True)
            for idx, record in topic_df.iterrows():
                # Only show Topic Sentence, Prompt, Response, Last Updated (if available)
                fields = [col for col in topic_df.columns if col not in ["id"]]
                # If Last Updated is not present, skip it
                record_dict = {field: record[field] for field in fields if field in record}
                # Convert to DataFrame for st.table, with field names as first column
                display_df = pd.DataFrame(record_dict.items(), columns=["Field", "Value"])
                st.dataframe(display_df, hide_index=True)