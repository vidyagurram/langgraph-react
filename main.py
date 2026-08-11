from dotenv import load_dotenv
from langgraph.graph import MessagesState, StateGraph, END
from langchain_core.messages import HumanMessage
from nodes import tool_node, run_agent_reasoning
import os

load_dotenv(override=True)
print("Hello There!!")
print(os.environ.get("TAVILY_API_KEY"))

AGENT_REASON = "agent_reason"
ACT= "act"
LAST = -1


def should_continue(state: MessagesState)->str:
    if not state["messages"]["LAST"].tool_calls:
        return END
    return ACT

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)

flow.add_conditional_edges(AGENT_REASON, should_continue, {
    END:END,
    ACT:ACT
})

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()
app.get_graph().draw_mermaid_png(output_file_path="agentFlow.png")



if __name__ == "__main__":
    print("Hello ReAct LangGraph with Function Calling")
    
