from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv(override=True)

@tool
def triple(num:float) -> float:
    """
    param num: an input number to get tripled
    result: triple of an input number
    """

    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)





