import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage, SystemMessage, AIMessage

from langchain.chat_models import init_chat_model
load_dotenv()



model =init_chat_model(
    model="gpt-4o",
    temperature=0,
)
conversation=[
    
    SystemMessage(content="you are the helful assistant that can provide weather information using the get_weather tool when necessary."),
HumanMessage(" what is python?"),
AIMessage("Python is a high-level, interpreted programming language known for its readability and versatility. It is widely used for web development, data analysis, artificial intelligence, scientific computing, and more." ),
HumanMessage(" when it was released ?")
] 

