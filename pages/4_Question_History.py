import streamlit as st

st.title("📝 Question History")

if st.button("🗑 Clear History"):

    st.session_state.question_history = []

    st.rerun()

history = st.session_state.get(
    "question_history",
    []
)

if not history:

    st.info(
        "No questions asked yet."
    )

else:

    for item in reversed(history):

        st.subheader(
            item["module"]
        )

        st.write(
            f"Question: {item['question']}"
        )

        st.write(
            f"Answer: {item['answer']}"
        )

        st.markdown("---")