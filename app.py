import streamlit as st
from Auth.login import login

st.set_page_config(
    page_title="AI Smart Building Assistant",
    page_icon="🏢"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "question_history" not in st.session_state:
    st.session_state.question_history = []

if not st.session_state.logged_in:

    login()

else:

    st.title("🏢 AI Smart Building Assistant")

    st.write(
        f"Welcome, {st.session_state.username}"
    )

    st.write(
        f"Role: {st.session_state.role}"
    )

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()