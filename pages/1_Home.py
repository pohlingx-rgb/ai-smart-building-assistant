import streamlit as st

st.title("🏢 Home Dashboard")

username = st.session_state.get("username", "Guest")
role = st.session_state.get("role", "Unknown")

st.success(f"Welcome, {username}")

st.info(f"Role: {role}")

st.markdown("---")

st.subheader("Project Overview")

st.write("""
AI Assistant for Smart Building Operations helps Facilities Management teams:

✅ Search Operational Manuals

✅ Search SOP Documents

✅ Search Contract Specifications

✅ Search Schedule of Rates (SOR)

✅ Ask questions using Natural Language

✅ Receive AI-generated answers with source references
""")

st.markdown("---")

st.subheader("Available Features")

st.write("""
📘 Operations Knowledge Assistant

🔍 SOR Validator

📝 Question History

ℹ️ About Us

⚙️ Methodology
""")

st.markdown("---")

st.subheader("Quick Navigation")

st.write("""
Use the menu on the left to navigate between pages.
""")

st.subheader("Current User")

st.write(
    f"Username: {st.session_state.username}"
)

st.write(
    f"Role: {st.session_state.role}"
)

if st.session_state.role == "Admin":

    st.success(
        "You have document upload privileges."
    )

else:

    st.info(
        "You have standard user access."
    )