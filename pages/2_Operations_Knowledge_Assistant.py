import streamlit as st
from datetime import datetime
import pandas as pd

from modules.document_loader import (
    read_pdf,
    read_docx,
    read_txt
)

from modules.text_splitter import split_text

from modules.rag_pipeline import generate_answer, generate_sor_answer

from vectorstore.faiss_manager import create_vector_store

st.title("📘 Operations Knowledge Assistant")

if "uploaded_documents" not in st.session_state:
    st.session_state["uploaded_documents"] = []

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

    document_info = {
    "name": file_name,
    "upload_time": datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    ),
    "size_kb": round(
        uploaded_file.size / 1024,
        2
    )
}
    existing_docs = [
        doc["name"]
        for doc in st.session_state.get("uploaded_documents", [])
    ]

    if file_name not in existing_docs:
        st.session_state["uploaded_documents"].append(
            document_info
        )

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

    st.markdown("---")

st.subheader("📂 Uploaded Document Library")

st.metric(
    "Total Documents",
    len(st.session_state["uploaded_documents"])
)

search_term = st.text_input(
    "🔍 Search uploaded documents"
)

df = pd.DataFrame(
    st.session_state["uploaded_documents"]
)

if not df.empty:

    if search_term:

        df = df[
            df["name"].str.contains(
                search_term,
                case=False,
                na=False
            )
        ]

    df.index = range(
        1,
        len(df) + 1
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info(
        "No documents uploaded yet."
    )
