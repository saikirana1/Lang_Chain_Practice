import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

@tool('get_weather', return_direct=False, description="Get the current weather for a given city.")
def get_weather(city: str) -> str:
    # """Fetches the current weather for the specified city using a mock API."""
    # # Mock API URL (replace with a real weather API endpoint)
    # api_url = f"https://wttr.in/{city}?format=j1"
    # response = requests.get(api_url)
    # if response.status_code == 200:
    #     data = response.json()
    #     return f"The current temperature in {city} is {data['temperature']}°C with {data['description']}."
    # else:
        return "temparture in vienna  today is 35 degree centigrade."
    
agent=create_agent(
    model="gpt-4o",
    tools=[get_weather],
    
    system_prompt="you are the helful assistant that can provide weather information using the get_weather tool when necessary."
)


res=agent.invoke({
    'messages': [
        {"role": "user", "content": "What is the weather like in vienna today?"}
    ]
}
    
    
)
print(res)