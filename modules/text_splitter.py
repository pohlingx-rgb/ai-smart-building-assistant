from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(document_text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(document_text)

    return chunks