import textwrap
import chromadb
import numpy as np
import pandas as pd

import google.generativeai as genai
import google.ai.generativelanguage as glm

from chromadb import Documents, EmbeddingFunction, Embeddings

import os

google_gemini_api_key = os.environ['GOOGLE_API_KEY']

for m in genai.list_models():
  if 'embedContent' in m.supported_generation_methods:
    print(m.name)

DOCUMENT1 = "Operating the Climate Control System  Your Googlecar has a climate control system that allows you to adjust the temperature and airflow in the car. To operate the climate control system, use the buttons and knobs located on the center console.  Temperature: The temperature knob controls the temperature inside the car. Turn the knob clockwise to increase the temperature or counterclockwise to decrease the temperature. Airflow: The airflow knob controls the amount of airflow inside the car. Turn the knob clockwise to increase the airflow or counterclockwise to decrease the airflow. Fan speed: The fan speed knob controls the speed of the fan. Turn the knob clockwise to increase the fan speed or counterclockwise to decrease the fan speed. Mode: The mode button allows you to select the desired mode. The available modes are: Auto: The car will automatically adjust the temperature and airflow to maintain a comfortable level. Cool: The car will blow cool air into the car. Heat: The car will blow warm air into the car. Defrost: The car will blow warm air onto the windshield to defrost it."
DOCUMENT2 = "Your Googlecar has a large touchscreen display that provides access to a variety of features, including navigation, entertainment, and climate control. To use the touchscreen display, simply touch the desired icon.  For example, you can touch the \"Navigation\" icon to get directions to your destination or touch the \"Music\" icon to play your favorite songs."
DOCUMENT3 = "Shifting Gears Your Googlecar has an automatic transmission. To shift gears, simply move the shift lever to the desired position.  Park: This position is used when you are parked. The wheels are locked and the car cannot move. Reverse: This position is used to back up. Neutral: This position is used when you are stopped at a light or in traffic. The car is not in gear and will not move unless you press the gas pedal. Drive: This position is used to drive forward. Low: This position is used for driving in snow or other slippery conditions."


documents = [DOCUMENT1, DOCUMENT2, DOCUMENT3]

class GeminiEmbeddingFunction(EmbeddingFunction):
  def __call__(self, input: Documents) -> Embeddings:
    model = 'models/embedding-001'
    title = "Custom query"
    return genai.embed_content(model=model,
                                content=input,
                                task_type="retrieval_document",
                                title=title)["embedding"]
  
def create_chroma_db(documents, name):
  chroma_client = chromadb.Client()
  db = chroma_client.create_collection(name=name, embedding_function=GeminiEmbeddingFunction())

  for i, d in enumerate(documents):
    db.add(
      documents=d,
      ids=str(i)
    )
  return db

db = create_chroma_db(documents, "googlecarsdatabase")

df = pd.DataFrame(db.peek(3))

# The scope of these changes made to
# pandas settings are local to with statement.
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)

def get_relevant_passage(query, db):
    passage = db.query(query_texts=[query], n_results=1)['documents'][0][0]
    return passage

# Perform embedding search
passage = get_relevant_passage("touch screen features", db)
print(passage)

def make_prompt(query, relevant_passage):
    escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = ("""You are a helpful and informative bot that answers questions using text from the reference passage included below. \
    Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
    However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
    strike a friendly and converstional tone. \
    If the passage is irrelevant to the answer, you may ignore it.
    QUESTION: '{query}'
    PASSAGE: '{relevant_passage}'

    ANSWER:
    """).format(query=query, relevant_passage=escaped)

    return prompt

query = "How do you use the touchscreen in the Google car?"
prompt = make_prompt(query, passage)
print(prompt)

model = genai.GenerativeModel('gemini-pro')
answer = model.generate_content(prompt)
print(answer.text)  