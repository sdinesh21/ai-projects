# CSV-Based AI Chatbot

## Introduction
This project introduces a unique AI chatbot agent capable of answering questions based on data from an uploaded CSV file. Utilizing OpenAI's language models along with Langchain and the Retrieval-Augmented Generation (RAG) approach, this chatbot offers an interactive way to explore and gain insights from structured data without the need for manual data analysis.

## Features
- Upload CSV files to dynamically train the chatbot on the provided data.
- Ask natural language questions and receive answers derived directly from the uploaded CSV content.
- Utilize OpenAI's powerful language models for accurate and context-aware responses.
- Simple and intuitive web interface built with Streamlit, making it accessible for users of all technical levels.

## Prerequisites
Before you can run this project, you'll need the following:
- Python 3.7 or later
- pip (Python package manager)
- An OpenAI API key

## Installation

1. **Clone the Repository**
<br><code>git clone https://github.com/sdinesh21/csv-based-ai-chatbot.git
cd csv-based-ai-chatbot</code>

2. **Install Dependencies**
Install the required Python packages using pip and the `REQUIREMENTS.txt` file:
<br>```pip install -r REQUIREMENTS.txt```


This command will automatically install all the dependencies listed in the `REQUIREMENTS.txt` file, including `streamlit`, `langchain`, `openai`, `streamlit-chat`, and any others specified.

3. **Set Up Your OpenAI API Key**
Obtain an API key from [OpenAI](https://openai.com/), and set it as an environment variable in your terminal session:
<br><code>export OPENAI_API_KEY='your_api_key_here'</code>

Alternatively, you can enter your API key directly through the application's interface when prompted.

## Running the Application

To launch the application, run the following command in your terminal:
<br><code>streamlit run app.py</code>

Navigate to the provided URL, usually http://localhost:8501, in your web browser to interact with the application.

## Usage

1. **API Key**: Enter your OpenAI API key in the sidebar when prompted.
2. **Upload CSV**: Use the sidebar option to upload a CSV file from which the chatbot will learn.
3. **Ask Questions**: After uploading, enter your questions in the input field to receive answers based on the CSV data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to OpenAI for providing access to their powerful language models.
- Appreciation to the developers of Langchain and Streamlit for their fantastic tools that made this project possible.
- Special thanks to all contributors who help improve and extend the capabilities of this chatbot.
