from langchain_community.vectorstores import FAISS

def create_vectorstore(chunks, embeddings):
    return FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )


def retrieve_documents(vectorstore, question, k=4):
    return vectorstore.similarity_search(question, k=k)