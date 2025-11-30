from app.adk.sdk import Broker
# Import agents and tools to register them via decorators on import
from app.adk.agents.writer_agent import writer
from app.adk.agents.reviewer_agent import reviewer
from app.adk.tools.search_tool import search

def create_broker():
    broker = Broker()
    # decorators already registered them; but we can re-register explicitly if desired
    broker.register_agent(writer)
    broker.register_agent(reviewer)
    broker.register_tool(search)
    return broker
