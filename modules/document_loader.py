from pypdf import PdfReader
from docx import Document


def read_pdf(uploaded_file):
    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def read_docx(uploaded_file):
    doc = Document(uploaded_file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def read_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")