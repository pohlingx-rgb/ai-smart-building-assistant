import streamlit as st
from datetime import datetime

from modules.rag_pipeline import generate_sor_answer

st.title("🔍 SOR Validator")

st.write("""
Ask questions about Schedule of Rates (SOR)
contracts and coverage.
""")

question = st.text_input("Enter SOR validation question")
vector_store = st.session_state.get("vector_store")
answer = ""
results = []

if question and vector_store:
    results = vector_store.similarity_search(question, k=3)
    answer = generate_sor_answer(question, results)

if "question_history" not in st.session_state:
    st.session_state.question_history = []

st.session_state.question_history.append(
    {
        "module": "Operations Assistant",
        "question": question,
        "answer": answer,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
)

st.subheader("SOR Assessment")
st.write(answer or "Enter a question to get an answer.")

st.subheader("Supporting Sources")
for idx, doc in enumerate(results):
    st.write(f"Source {idx + 1}")
    st.code(doc.page_content)

# current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")