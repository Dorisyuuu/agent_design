# Simple local ADK-like shim for learning purposes.
# Provides decorators for tools and agents and a lightweight Broker.

from typing import Callable, Dict, Any, List

TOOLS: Dict[str, Callable] = {}
AGENTS: Dict[str, Callable] = {}

def tool(fn: Callable):
    TOOLS[fn.__name__] = fn
    return fn

def agent(fn: Callable):
    AGENTS[fn.__name__] = fn
    return fn

class Broker:
    def __init__(self):
        self.tools = TOOLS
        self.agents = AGENTS
    def register_tool(self, fn):
        self.tools[fn.__name__] = fn
    def register_agent(self, fn):
        self.agents[fn.__name__] = fn
    def call_tool(self, name: str, *args, **kwargs):
        fn = self.tools.get(name)
        if not fn:
            raise RuntimeError(f"Tool {name} not found")
        return fn(*args, **kwargs)
    def call_agent(self, name: str, *args, **kwargs):
        fn = self.agents.get(name)
        if not fn:
            raise RuntimeError(f"Agent {name} not found")
        return fn(*args, **kwargs)
    def run_pipeline(self, pipeline: str, input_data: str):
        # pipeline like "writer->reviewer"
        steps = [s.strip() for s in pipeline.split("->")]
        data = input_data
        for step in steps:
            if step in self.agents:
                data = self.call_agent(step, data)
            elif step in self.tools:
                data = self.call_tool(step, data)
            else:
                raise RuntimeError(f"Step {step} not recognized as agent or tool.")
        return data
