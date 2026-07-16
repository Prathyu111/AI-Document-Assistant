import os
import streamlit as st
from dotenv import load_dotenv

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.embeddings import get_embeddings
from utils.retriever import create_vectorstore, retrieve_documents
from utils.gemini_client import get_llm

load_dotenv()

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Document Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Reading PDF..."):
        text = load_pdf(uploaded_file)

    st.success("PDF Loaded Successfully!")

    chunks = split_text(text)

    embeddings = get_embeddings()

    vectorstore = create_vectorstore(
        chunks,
        embeddings
    )

    question = st.text_input(
        "Ask a question about your document"
    )

    if st.button("Ask"):

        docs = retrieve_documents(
            vectorstore,
            question
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the information below.

Context:

{context}

Question:

{question}
"""

        llm = get_llm()

        response = llm.invoke(prompt)

        st.subheader("Answer")

        st.write(response.content)

        with st.expander("Retrieved Context"):

            st.write(context)