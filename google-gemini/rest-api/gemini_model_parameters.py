from requests

import sys
# setting path
sys.path.append('../google-gemini')
from google-gemini.config import API_KEY

def send_prompt_to_gemini(prompt_text, parameters):
    api_endpoint = "https://REGION-gemini.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/REGION/endpoints/YOUR_ENDPOINT_ID:predict"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY" 
    }

    payload = {
        "instances": [{"text": prompt}],
        "parameters": parameters 
    }

    response = requests.post(api_endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['predictions'][0]['text']
    else:
        raise Exception(f"API request failed with status code: {response.status_code}")


# Example 1: Focused Response
prompt = "What is the capital of France?"
parameters = {
    "max_output_tokens": 20, 
    "temperature": 0.2,  
    "topK": 5,   
    "topP": 0.95 
}
response = send_prompt_to_gemini(prompt, parameters)
print(response)  # Likely output: "Paris" 

# Example 2: Creative Response
prompt = "Write the start of a story about a robot who discovers friendship."
parameters = {
    "max_output_tokens": 100,
    "temperature": 0.8,
    "topK": 40,
    "topP": 0.7
}
response = send_prompt_to_gemini(prompt, parameters)
print(response)  # Could be a variety of creative openings
