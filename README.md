# ADK + LangGraph + LangChain Demo

这是一个学习与实践示例项目，包含三部分：
- **LangChain**: 基本的 LLMChain 示例
- **LangGraph**: 简单的 StateGraph workflow 示例
- **ADK (local shim for learning)**: 一个轻量级的本地 Agent Developer Kit 风格实现（用于学习，不依赖 Google 官方库）

说明：
- 项目提供示例代码与 FastAPI 接口，便于本地学习与扩展。
- 若要接入真实 LLM（OpenAI 等），请在环境变量 `OPENAI_API_KEY` 中填入你的 API key，并在 `config/settings.py` 中根据需要修改 model 名称或提供真实 provider。

运行：
1. 创建虚拟环境并安装依赖：
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. 启动 FastAPI：
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
3. API:
   - POST /api/chain/basic  -> LangChain 示例
   - POST /api/graph/generate -> LangGraph workflow
   - POST /api/adk/run -> 简化 ADK (writer -> reviewer)

项目结构见下（或查看仓库）.

