from app.adk.sdk import agent
from app.services.llm_provider import get_llm

@agent
def reviewer(draft: str) -> str:
    llm = get_llm()
    try:
        out = llm.predict(f"请对以下初稿进行审阅并给出修改稿:\n{draft}")
    except Exception:
        out = llm(f"请对以下初稿进行审阅并给出修改稿:\n{draft}")
    return "[REVIEWER]\n" + out
