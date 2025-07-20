from llama_index.core.agent import FunctionCallingAgent
from llama_index.core.tools import FunctionTool
from mcp import Client

from mcp_server import add_data, fetch_data

def build_agent():
    client = Client()
    tools = [FunctionTool.from_defaults(fn=add_data),
             FunctionTool.from_defaults(fn=fetch_data)]

    agent = FunctionCallingAgent.from_tools(tools, system_prompt="Use the tools to answer user queries before responding.")
    return agent
