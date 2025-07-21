# app.py
import streamlit as st
from db_utils import init_db

import pages.Home as Home
import pages.New_Curriculum as New_Curriculum
import pages.Display as Display

# Initialize database
init_db()

st.set_page_config(page_title="Curriculum Builder", layout="centered")

page = st.navigation([
    st.Page(Home.show, title="Home", icon="🏠"),
    st.Page(New_Curriculum.show, title="New Curriculum", icon="📝"),
    st.Page(Display.show, title="Display", icon="📄"),
])

page.run()