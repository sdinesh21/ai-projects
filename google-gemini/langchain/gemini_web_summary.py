# Run this cell and paste the API key in the prompt
import os
import getpass

from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain.schema import StrOutputParser
from langchain.schema.prompt_template import format_document

from langchain_google_genai import ChatGoogleGenerativeAI

google_gemini_api_key = os.environ['GOOGLE_API_KEY']

loader = WebBaseLoader("https://blog.google/technology/ai/google-gemini-update-sundar-pichai-2024/")
docs = loader.load()

# print(docs)

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, top_p=0.85)

# To extract data from WebBaseLoader
doc_prompt = PromptTemplate.from_template("{page_content}")

# To query Gemini
llm_prompt_template = """Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:"""
llm_prompt = PromptTemplate.from_template(llm_prompt_template)

print(llm_prompt)

stuff_chain = (
    # Extract data from the documents and add to the key `text`.
    {
        "text": lambda docs: "\n\n".join(
            format_document(doc, doc_prompt) for doc in docs
        )
    }
    | llm_prompt         # Prompt for Gemini
    | llm                # Gemini function
    | StrOutputParser()  # output parser
)

result = stuff_chain.invoke(docs)

print (result)

