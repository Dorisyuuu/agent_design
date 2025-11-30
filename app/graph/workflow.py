from langgraph.graph import StateGraph
from app.graph.state import GraphState
from app.graph.nodes.generate_node import generate_node
from app.graph.nodes.refine_node import refine_node

def create_workflow():
    graph = StateGraph(GraphState)
    graph.add_node("generate", generate_node)
    graph.add_node("refine", refine_node)
    graph.add_edge("generate", "refine")
    graph.set_entry_point("generate")
    return graph.compile()
