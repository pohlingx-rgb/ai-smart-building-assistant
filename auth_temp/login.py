import streamlit as st


def login():

    users = {
        "admin": {
            "password": "admin123",
            "role": "Admin"
        },
        "user": {
            "password": "user123",
            "role": "User"
        }
    }

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username in users:

            if password == users[username]["password"]:

                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = users[username]["role"]

                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Wrong Password")

        else:
            st.error("User Not Found")
            