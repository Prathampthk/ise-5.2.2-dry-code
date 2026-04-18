import streamlit as st

def initialize_session():
    """Initializes the session state for authentication."""
    if st.session_state.get("logged_in") is None:
        st.session_state["logged_in"] = False

def login():
    st.session_state.logged_in = True

def logout():
    st.session_state.logged_in = False

def render_sidebar():
    """Renders the authentication buttons and copyright in the sidebar."""
    initialize_session()
    
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout) # Added key here
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login) # Added key here

    st.sidebar.write("This site is copyright Fake Company LLC Inc., 2024")

def render_footer():
    """Renders the company info and links expanders at the bottom of the page."""
    with st.expander("Company Info"):
        st.write(
            """
            Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
        """
        )

    with st.expander("Links"):
        st.markdown(
            """
            [Google](https://google.com)

            [Gemini](https://gemini.google.com)

            [Streamlit Docs](https://docs.streamlit.io/)
        """
        )