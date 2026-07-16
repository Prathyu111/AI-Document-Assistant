 # 🤖 AI Document Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions using Google Gemini.

## Features

- Upload PDF documents
- Extract text
- Semantic search using FAISS
- Google Gemini responses
- Local embeddings
- Streamlit interface

## Tech Stack

- Python
- Streamlit
- Google Gemini
- Sentence Transformers
- FAISS
- LangChain
- PyPDF

## Installation

```bash
pip install -r requirements.txt
```

Create:

```
.env
```

```
GOOGLE_API_KEY=YOUR_KEY
```

Run:

```bash
streamlit run app.py
```

## Future Improvements

- Multiple PDFs
- Chat history
- Citations
- Docker
- Authentication