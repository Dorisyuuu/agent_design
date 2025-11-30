from fastapi import APIRouter
from app.models.request_models import GenerateRequest, GenerateResponse
from app.graph.workflow import create_workflow
from app.chains.basic_chain import create_basic_chain

router = APIRouter()
workflow = create_workflow()
simple_chain = create_basic_chain()

@router.post("/graph/generate", response_model=GenerateResponse)
def run_graph(req: GenerateRequest):
    result = workflow.invoke({"user_input": req.input})
    return GenerateResponse(draft=result["draft"], refined=result["refined"])

@router.post("/chain/basic")
def run_chain(req: GenerateRequest):
    result = simple_chain.run(topic=req.input)
    return {"output": result}
