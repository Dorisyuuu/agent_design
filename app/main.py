from fastapi import FastAPI
from app.api.router import router

app = FastAPI(title="ADK + LangGraph + LangChain Demo")
app.include_router(router, prefix="/api")
