from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_community.tools import TavilySearchResults
import datetime

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


tools = [search_tool, get_system_time]

agent = create_agent(
    model=llm, 
    tools=tools,
    system_prompt="You are a helpful assistant with access to web search and system time tools."
)

agent.invoke({"input": "When was SpaceX's last launch and how many days ago was that from this instant"})

