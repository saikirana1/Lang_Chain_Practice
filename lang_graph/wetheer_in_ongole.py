from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults

load_dotenv()

def wetheer_in_ongole():

    llm = ChatOpenAI(
        model="gpt-4o",
        
    )
    serch_tool = TavilySearchResults(search_depth="basic")
    agent = create_agent(
        llm=llm,
        model="gpt-4o",
        tools=[serch_tool],
        system_prompt="You are a helpful assistant that can use the available tools to answer user queries.",
        agent="zero-shot-react-description",
    )

    response = agent.invoke({
        "input": "What is the weather like in Ongole today?",
    })
    print(response)
    return response