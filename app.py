import streamlit as st
from utils import render_sidebar, render_footer

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

render_sidebar()

st.write("# Welcome to Streamlit!")

st.markdown(
    """
    This website has a lot of redundant code. Can you find it and create a utility file which contains the redundancies?
    """
)

render_footer()