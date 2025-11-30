from app.services.llm_provider import get_llm
from app.graph.state import GraphState

def refine_node(state: GraphState) -> GraphState:
    llm = get_llm()
    try:
        refined = llm.predict(f"请润色以下草稿:\n{state.draft}")
    except Exception:
        refined = llm(f"请润色以下草稿:\n{state.draft}")
    return GraphState(user_input=state.user_input, draft=state.draft, refined=refined)
