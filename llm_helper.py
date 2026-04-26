from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

import os
from langchain_groq import ChatGroq

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant"
)

if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)
