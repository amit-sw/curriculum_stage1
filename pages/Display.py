# pages/Display.py
import streamlit as st
import pandas as pd
from db_utils import get_all_curriculums

def show_display():
    st.header("Saved Curricula")
    data = get_all_curriculums()
    if not data:
        st.info("No curricula found.")
        return

    df = pd.DataFrame(data, columns=["ID", "Topic Sentence", "Topic", "Prompt", "Response"])
    truncated_df = df.applymap(lambda x: str(x).splitlines()[0] if isinstance(x, str) else x)

    table_html = "<table style='width:100%; border-collapse: collapse;'>"
    # Header
    table_html += "<thead><tr>" + "".join(f"<th style='border:1px solid #ddd;padding:8px'>{col}</th>" for col in truncated_df.columns) + "</tr></thead>"
    table_html += "<tbody>"
    for i, row in truncated_df.iterrows():
        table_html += "<tr>"
        for col in truncated_df.columns:
            short = row[col]
            full = df.loc[i, col]
            cell_html = (
                f"<details style='cursor:pointer'><summary>{short}</summary>"
                f"<pre style='white-space:pre-wrap'>{full}</pre></details>"
            )
            table_html += f"<td style='border:1px solid #ddd;padding:8px;vertical-align:top'>{cell_html}</td>"
        table_html += "</tr>"
    table_html += "</tbody></table>"

    st.markdown(table_html, unsafe_allow_html=True)