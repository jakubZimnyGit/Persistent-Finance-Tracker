import streamlit as st
from app.database import init_db

if __name__ == "__main__":
    init_db()

    st.title("Persistent Finance Tracker")
    st.write("Welcome to the Persistent Finance Tracker! Use the sidebar to navigate through different features.")
