# app.py
import streamlit as st
from db_utils import init_db

# Initialize database
init_db()

st.set_page_config(page_title="Curriculum Builder", layout="centered")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "New Curriculum", "Display"])

if page == "Home":
    import pages.Home as Home
    Home.show()
elif page == "New Curriculum":
    import pages.New_Curriculum as New_Curriculum
    New_Curriculum.show()
elif page == "Display":
    import pages.Display as Display
    Display.show()