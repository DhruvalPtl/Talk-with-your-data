import google.generativeai as genai
genai.configure(api_key="")
model = genai.GenerativeModel(model="gemini-1.5-flash")
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages) 