from app.adk.sdk import agent
from app.services.llm_provider import get_llm

@agent
def writer(prompt: str) -> str:
    llm = get_llm()
    try:
        out = llm.predict(f"写一篇基于以下提示的初稿:\n{prompt}")
    except Exception:
        out = llm(f"写一篇基于以下提示的初稿:\n{prompt}")
    return "[WRITER]\n" + out
