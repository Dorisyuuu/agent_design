# This example assumes a minimal API for langgraph.StateGraph.
# If your installed langgraph package exposes a different API, adapt accordingly.

from app.graph.state import GraphState
from app.graph.nodes.generate_node import generate_node
from app.graph.nodes.refine_node import refine_node

# Minimal shim: if langgraph is available, use it; otherwise provide a tiny execution wrapper.
try:
    from langgraph.graph import StateGraph
    def create_workflow():
        graph = StateGraph(GraphState)
        graph.add_node("generate", generate_node)
        graph.add_node("refine", refine_node)
        graph.add_edge("generate", "refine")
        graph.set_entry_point("generate")
        return graph.compile()
except Exception:
    class SimpleWorkflow:
        def __init__(self):
            pass
        def invoke(self, state_dict):
            state = GraphState(**state_dict)
            state = generate_node(state)
            state = refine_node(state)
            return state.dict()
    def create_workflow():
        return SimpleWorkflow()
