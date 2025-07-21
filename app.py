# app.py
import streamlit as st
from db_utils import init_db

import pages.Home as Home
import pages.New_Curriculum as New_Curriculum
import pages.Display as Display
import pages.Modify_Curriculum as Modify_Curriculum

# Initialize database
init_db()

st.set_page_config(page_title="Curriculum Builder", layout="centered")

page = st.navigation([
    st.Page(Home.show_home, title="Home", icon="🏠"),
    st.Page(New_Curriculum.show_new_curriculum, title="New Curriculum", icon="📝"),
    st.Page(Display.show_display, title="Display", icon="📄"),
    st.Page(Modify_Curriculum.show_modify_curriculum, title="Modify Curriculum", icon="✏️"),
])

page.run()