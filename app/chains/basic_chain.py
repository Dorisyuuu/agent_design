from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.services.llm_provider import get_llm

def create_basic_chain():
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="请根据主题 {topic} 生成一段简介。",
    )
    return LLMChain(prompt=prompt, llm=get_llm())
