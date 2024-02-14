from langchain_community.document_loaders import WebBaseLoader
from unstructured.cleaners.core import remove_punctuation,clean,clean_extra_whitespace
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain

from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI

loader = WebBaseLoader("https://www.cnet.com/tech/home-entertainment/deadpool-3-super-bowl-trailer-shows-wade-wilson-with-the-tva/#ftag=CAD590a51e")
docs = loader.load()

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106",openai_api_key='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')
chain = load_summarize_chain(llm, chain_type="stuff")

summary = chain.run(docs)

print(summary)