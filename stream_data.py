from langchain.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()

model=init_chat_model(
    model="gpt-4o",
    temperature=0,
)
for chunk in model.stream("hellow what is langchain?"):
    print(chunk.text, end='', flush=True)
    
