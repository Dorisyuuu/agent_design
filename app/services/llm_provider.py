from langchain_openai import ChatOpenAI
from config.settings import settings

def get_llm():
    return ChatOpenAI(
        model=settings.model_name,
        temperature=0.7,
        api_key=settings.openai_api_key
    )
