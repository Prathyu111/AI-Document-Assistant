 # 🤖 AI Document Assistant

# 🤖 AI Document Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions using Google Gemini.

---

## ✨ Features

- 📄 Upload PDF documents
- 🔍 Semantic search using FAISS
- 🧠 Local embeddings with Sentence Transformers
- 🤖 Google Gemini integration
- 💬 Natural language question answering
- 📚 Retrieved context display
- ⚡ Streamlit web interface

---

## 🏗️ Architecture

PDF
↓
PDF Loader
↓
Text Chunking
↓
Sentence Transformers
↓
FAISS Vector Store
↓
Retriever
↓
Google Gemini
↓
Answer

---

## 📸 Screenshots

### Home Screen

!Content.png

### Upload PDF

!Pdf upload.png

### AI Answer

![Answer] Summarize.png

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Google Gemini
- PyPDF

---

## 🚀 Installation

```bash
git clone https://github.com/Prathyu111/AI-Document-Assistant.git

cd AI-Document-Assistant

pip install -r requirements.txt

streamlit run app.py


## Experiments

These scripts were used during development to:

- Verify Gemini API connectivity
- Test available Gemini models
- Validate API responses independently from the Streamlit application

These are development utilities and are not required to run the application.

