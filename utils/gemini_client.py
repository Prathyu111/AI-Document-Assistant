from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        temperature=0,
        max_retries=5
    )