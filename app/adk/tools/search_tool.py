from app.adk.sdk import tool

@tool
def search(query: str) -> str:
    # Placeholder: integrate a real search / RAG in production
    return f"[SEARCH] 模拟搜索结果: {query}"
