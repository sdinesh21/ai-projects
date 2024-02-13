import http.client, urllib.parse
import json
import os


from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="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"
)

conn = http.client.HTTPSConnection('api.thenewsapi.com')
article_conn = http.client.HTTPSConnection('api.articlextractor.com')

params = urllib.parse.urlencode({
    'api_token': 'oMQLlh5HIf0aox5xDWBqN4UDDduVGrodiZNdfghU',
    'categories': 'tech',
    'limit': 2,
    'language': 'en'
    })

conn.request('GET', '/v1/news/all?{}'.format(params))

res = conn.getresponse()
data = res.read()

# url = data.url.decode('utf-8')

# Parse the JSON data
data_object = json.loads(data)
news_data = data_object['data']

# Iterate over each item in the list and print the desired fields
for item in news_data:
    news_url = item['url']
    print("URL:", item['url'])

article_params = urllib.parse.urlencode({
    'api_token': 'NDzrgqyapRIDeDCproG5cer75sbGqUpQeeAU37pW',
    'url': news_url,
    })
article_conn.request('GET', '/v1/extract?{}'.format(article_params))
article_res = article_conn.getresponse()
article_data = article_res.read()
article_data_object = json.loads(article_data)
article_data = article_data_object['data']


article_text = article_data['text']
# Iterate over each item in the list and print the desired fields
# for article_item in article_data:
    # print (article_item)
    # print("Text:", article_item['text'])

# Sending a request to the OpenAI API to summarize the text
response = client.chat.completions.create(
  model="gpt-3.5-turbo",  # Updated model name, adjust based on availability and your needs
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Summarize the following text:\n\n{article_text}"}
    ]
)

# Printing the summarized text
print(response)
# print(response.choices[0].message['content'].strip())