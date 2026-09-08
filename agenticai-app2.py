# Open AI SDK

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="tell me about openai sdk in short",
)

print(response.output_text)