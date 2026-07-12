# AI Assistant for Smart Building Operations

## Project Overview

This project helps Facilities Management (FM) teams search Operational Manuals, SOPs, Contract Specifications, and Schedule of Rates (SOR) documents using AI.

The solution uses Retrieval-Augmented Generation (RAG) with OpenAI and FAISS.

---

## Features

### Operations Knowledge Assistant

- Upload FM documents
- Ask natural language questions
- Receive AI-generated answers
- View source references

### SOR Validator

- Validate maintenance and repair items
- Assess contract coverage
- Retrieve supporting evidence

### Question History

- View previous questions and responses

### User Roles

Admin:
- Upload documents
- Ask questions
- Use SOR Validator

User:
- Ask questions
- Use SOR Validator

---

## Technology Stack

- Streamlit
- OpenAI
- LangChain
- FAISS
- Python

---

## Running Locally

### Install packages

```bash
pip install -r requirements.txt
```

### Start application

```bash
streamlit run app.py
```

---

## Default Users

Admin

Username:

```text
admin
```

Password:

```text
admin123
```

User

Username:

```text
user
```

Password:

```text
user123
```