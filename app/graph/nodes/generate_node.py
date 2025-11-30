from app.services.llm_provider import get_llm
from app.graph.state import GraphState

def generate_node(state: GraphState) -> GraphState:
    llm = get_llm()
    draft = llm.predict(f"请根据以下内容生成草稿:\n{state.user_input}")
    return GraphState(user_input=state.user_input, draft=draft, refined=state.refined)
