import streamlit as st
from dotenv import load_dotenv

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.embeddings import get_embeddings
from utils.retriever import create_vectorstore, retrieve_documents
from utils.gemini_client import get_llm

load_dotenv()


@st.cache_resource
def build_vectorstore(text):
    """Build FAISS vector store once per uploaded document."""
    chunks = split_text(text)
    embeddings = get_embeddings()
    return create_vectorstore(chunks, embeddings)


st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Document Assistant")
st.write("Upload a PDF and ask questions about its contents.")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Reading PDF..."):
        text = load_pdf(uploaded_file)

    if not text.strip():
        st.error("No readable text was found in this PDF.")
        st.stop()

    st.success("✅ PDF Loaded Successfully!")

    with st.spinner("Creating knowledge base..."):
        vectorstore = build_vectorstore(text)

    question = st.text_input(
        "Ask a question about your document",
        placeholder="Example: Summarize this document"
    )

    if question:

        docs = retrieve_documents(vectorstore, question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

If the answer is not present in the context, respond with:

"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}
"""

        llm = get_llm()

        try:

            with st.spinner("Thinking..."):
                response = llm.invoke(prompt)

            st.subheader("🤖 Answer")
            if isinstance(response.content, str):
                st.markdown(response.content)
            else:
                for item in response.content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        st.markdown(item["text"])

            with st.expander("📄 Retrieved Context"):
                st.write(context)

        except Exception as e:

            st.error("Unable to generate a response from Gemini.")
            st.exception(e)