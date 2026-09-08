# Langchain with memory management

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

messages = [
        # Setting context/behaviour

        SystemMessage(
        content="You are a python trainer. Answer in three short bullet points, also answer only python related question, if someone ask about java or AI or any other politely say I can answer only python queries."
    ),

      HumanMessage(
        content="Why should I learn python?"
    )
]

response = model.invoke(messages)
print("Content :", response.content)
print("Tokens  :", response.usage_metadata)
print("Model   :", response.response_metadata.get("model_name"))

messages.append(response)

messages.append(
    HumanMessage(
        content="Now give me the first thing I should build."
    )
)

response=model.invoke(messages)
print("------------------------------")
print("Content :", response.content)
print("------------------------------")
print("Tokens  :", response.usage_metadata)



