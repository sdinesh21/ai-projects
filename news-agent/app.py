import http.client, urllib.parse
import json
import os, streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.llms.openai import OpenAI
from langchain.chains.summarize import load_summarize_chain

# Streamlit app
st.subheader('News Feed Summary')

# Get OpenAI API key and source text input
openai_api_key = st.text_input("OpenAI API Key", type="password")
total_news = st.selectbox(
   "How many news articles do you need?",
   ("1", "2"),
   index=None,
   placeholder="Select a number",
)
category = st.selectbox(
   "Which category articles are you interested in?",
   ("sports", "business","entertainment","tech","food","travel"),
   index=None,
   placeholder="Select a category",
)

# If the 'Summarize' button is clicked
if st.button("Fetch"):
    # Validate inputs
    if not openai_api_key.strip() or not total_news.strip():
        st.error(f"Please provide the missing fields.")
    else:
        try:
            with st.spinner('Please wait...'):
              
              conn = http.client.HTTPSConnection('api.thenewsapi.com')
              article_conn = http.client.HTTPSConnection('api.articlextractor.com')

              params = urllib.parse.urlencode({
                    'api_token': 'oMQLlh5HIf0aox5xDWBqN4UDDduVGrodiZNdfghU',
                    'categories': 'tech',
                    'limit': total_news,
                    'language': 'en',
                    'categories' : category,
                    'published_on' : '2024-02-11'
                  })

              conn.request('GET', '/v1/news/top?{}'.format(params))

              res = conn.getresponse()
              data = res.read()

              # Parse the JSON data
              data_object = json.loads(data)
              news_data = data_object['data']

              # Iterate over each item in the list and print the desired fields
              for item in news_data:
                    news_url = item['url']
                    # print(item)
                    print(news_url)

                    article_params = urllib.parse.urlencode({
                            'api_token': 'NDzrgqyapRIDeDCproG5cer75sbGqUpQeeAU37pW',
                            'url': news_url,
                            'language': 'en'
                        })
                    article_conn.request('GET', '/v1/extract?{}'.format(article_params))
                    article_res = article_conn.getresponse()
                    article_data = article_res.read()
                    article_data_object = json.loads(article_data)

                    print(article_data_object)

                    article_json = article_data_object['data']

                    print("----------------------------------")

                    article_text = article_json['text']
                    # Iterate over each item in the list and print the desired fields
                    # for article_item in article_data:
                        # print (article_item)
                        # print("Text:", article_item['text'])

                    article_text_trim = article_text[:500]

                    # Split the source text
                    text_splitter = CharacterTextSplitter()
                    texts = text_splitter.split_text(article_text_trim)
                    # Create Document objects for the texts (max 3 pages)
                    docs = [Document(page_content=t) for t in texts[:3]]
                    # Initialize the OpenAI module, load and run the summarize chain
                    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
                    chain = load_summarize_chain(llm, chain_type="map_reduce")
                    summary = chain.run(docs)

              st.success(summary)
        except Exception as e:
            st.exception(f"An error occurred: {e}")