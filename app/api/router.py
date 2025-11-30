from fastapi import APIRouter
from app.models.request_models import GenerateRequest, GenerateResponse
from app.graph.workflow import create_workflow
from app.chains.basic_chain import create_basic_chain
from app.adk.broker import create_broker

router = APIRouter()
workflow = create_workflow()
simple_chain = create_basic_chain()

@router.post("/graph/generate", response_model=GenerateResponse)
def run_graph(req: GenerateRequest):
    result = workflow.invoke({"user_input": req.input})
    return GenerateResponse(draft=result.get("draft",""), refined=result.get("refined",""))

@router.post("/chain/basic")
def run_chain(req: GenerateRequest):
    result = simple_chain.run(topic=req.input)
    return {"output": result}

@router.post("/adk/run")
def run_adk(req: GenerateRequest):
    broker = create_broker()
    # run writer then reviewer via the broker
    result = broker.run_pipeline("writer->reviewer", req.input)
    return {"result": result}
