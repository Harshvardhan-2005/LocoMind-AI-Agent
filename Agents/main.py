import sys
import os
from dotenv import load_dotenv

load_dotenv()
from typing import (
    Annotated,
    Sequence,
    TypedDict
)
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage
)

from langchain_ollama import ChatOllama

from langgraph.graph.message import add_messages

from langgraph.graph import (
    StateGraph,
    END
)

gemini_model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai"
)

from langgraph.prebuilt import ToolNode

load_dotenv()

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        'tools'
    )
)

from tools import (
    add,
    subtract,
    multiply,
    create_file,
    write_file,
    search_duckduckgo,
    ingest_document,
    ask_rag,
    get_weather,
)

class AgentState(TypedDict):

    messages: Annotated[
        Sequence[BaseMessage],
        add_messages
    ]
tools = [
    add,
    subtract,
    multiply,
    create_file,
    write_file,
    search_duckduckgo,
    ingest_document,
    ask_rag,
    get_weather
]
gemini_model = gemini_model.bind_tools(tools)

model = ChatOllama(
    model="qwen3:4b",
    temperature=0
).bind_tools(tools)

def model_call(state: AgentState):

    system_prompt = SystemMessage(
        content="""
        You are a helpful AI assistant.
        Use tools intelligently when required.
        """
    )

    try:

        response = model.invoke(
            [system_prompt] + state["messages"]
        )

    except Exception:

        print("Local model failed. Switching to Gemini...")

        response = gemini_model.invoke(
            [system_prompt] + state["messages"]
        )

    return {
        "messages": [response]
    }

def should_continue(state: AgentState):

    last_message = state["messages"][-1]

    if (
        hasattr(last_message, "tool_calls")
        and last_message.tool_calls
    ):
        return "continue"

    return "end"

graph = StateGraph(AgentState)
graph.add_node(
    "our_agent",
    model_call
)

graph.add_node(
    "tools",
    ToolNode(tools=tools)
)
graph.set_entry_point("our_agent")

graph.add_conditional_edges(
    "our_agent",

    should_continue,

    {
        "continue": "tools",
        "end": END
    }
)

graph.add_edge(
    "tools",
    "our_agent"
)
app = graph.compile()
def print_stream(stream):

    for s in stream:

        message = s["messages"][-1]

        if hasattr(message, "content"):

            print(message.content)

inputs = {
    "messages": [
        HumanMessage(
          content="What's the weather in Delhi?"
        )
    ]
}

print_stream(
    app.stream(
        inputs,
        stream_mode="values"
    )
)