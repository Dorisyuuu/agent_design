from config.settings import settings

# NOTE: This file provides a thin wrapper. You can replace with real LangChain/OpenAI adapter.
try:
    from langchain_openai import ChatOpenAI
    def get_llm():
        return ChatOpenAI(model=settings.model_name, temperature=0.7, api_key=settings.openai_api_key)
except Exception:
    # Fallback: a dummy LLM object for local testing without external calls
    class DummyLLM:
        def predict(self, prompt: str) -> str:
            return "DUMMY_RESPONSE: " + (prompt[:200] + ("..." if len(prompt)>200 else ""))
        def __call__(self, prompt: str) -> str:
            return self.predict(prompt)
    def get_llm():
        return DummyLLM()
