import streamlit as st

from modules.document_loader import (
    read_pdf,
    read_docx,
    read_txt
)

from modules.text_splitter import split_text

from modules.rag_pipeline import generate_answer, generate_sor_answer

from vectorstore.faiss_manager import create_vector_store

st.title("📘 Operations Knowledge Assistant")

uploaded_file = None

if st.session_state.role == "Admin":

    uploaded_file = st.file_uploader(
        "Upload FM Document",
        type=["pdf", "docx", "txt"]
    )

else:

    st.info(
        "Document upload is restricted to Admin users."
    )

if uploaded_file:

    file_name = uploaded_file.name

    if file_name.endswith(".pdf"):
        text = read_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        text = read_docx(uploaded_file)

    elif file_name.endswith(".txt"):
        text = read_txt(uploaded_file)

    st.success("Document Uploaded Successfully")

    st.subheader("Document Name")
    st.write(file_name)

    st.subheader("Extracted Text Preview")
    st.text(text[:2000])

    chunks = split_text(text)

    st.session_state["document_text"] = text
    st.session_state["chunks"] = chunks

    st.subheader("Generated Chunks")
    st.write(f"Total Chunks: {len(chunks)}")

    vector_store = create_vector_store(chunks)

    st.session_state["vector_store"] = vector_store

    st.success("✅ FAISS Vector Store Created")

if "vector_store" not in st.session_state:

    st.warning(
        "No document database available. "
        "Please ask an Admin to upload documents."
    )

    st.stop()
# If there's no vector store, stop execution after warning.

# Ask question about the uploaded document
question = st.text_input(
    "Ask a question about the uploaded document"
)

from datetime import datetime

if question:
    results = st.session_state["vector_store"].similarity_search(question, k=3)
    answer = generate_answer(question, results)

    if "question_history" not in st.session_state:
        st.session_state["question_history"] = []

    st.session_state.question_history.append(
        {
            "module": "Operations Assistant",
            "question": question,
            "answer": answer,
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }
    )

    st.subheader("AI Answer")
    st.markdown(answer)

    st.subheader("Source References")
    for idx, doc in enumerate(results):
        st.write(f"Source {idx + 1}")
        st.code(doc.page_content)

# current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
