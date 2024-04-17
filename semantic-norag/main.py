import os
import streamlit as st
import tempfile
import traceback
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Streamlit page setup
def process_pdf():
    try:
        st.title("PDF Processing with AI")

        # Get OpenAI API key from user
        api_key = st.text_input("Enter your OpenAI API Key", type="password")
        if api_key:
            uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], key="pdf_uploader")

            if uploaded_file is not None:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    temp_pdf_path = tmp_file.name

                st.write('Loading document...')
                loader = PyPDFLoader(temp_pdf_path)
                data = loader.load()
                os.unlink(temp_pdf_path)  # Remove the temporary file after loading

                st.write(f'You have loaded a PDF with {len(data)} pages')

                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
                texts = [t.page_content for t in text_splitter.split_documents(data)]

                st.write('Indexing document...')

                # Create TF-IDF vectors for the chunks
                vectorizer = TfidfVectorizer()
                tfidf_matrix = vectorizer.fit_transform(texts)

                st.success('Indexing complete!')

                st.title('Document Answering with Langchain')
                usr_input = st.text_input('What is your question?')

                llm_chat = ChatOpenAI(temperature=0.9, max_tokens=150,
                                      model='gpt-3.5-turbo-0613', api_key=api_key)
                
                # Create chain
                chain = load_qa_chain(llm_chat)

                if usr_input:
                    query_vec = vectorizer.transform([usr_input])
                    cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
                    top_indices = cosine_sim.argsort()[-3:][::-1]  # Top 3 results

                    # Retrieve the most relevant chunks
                    relevant_texts = [texts[i] for i in top_indices]
                    # response = llm_chat.complete(prompt=usr_input + "\n".join(relevant_texts))
                    response = chain.run(input_documents=relevant_texts, question=usr_input)

                    st.write(response)
                    with st.expander('Top Relevant Chunks'):
                        for text in relevant_texts:
                            st.write(text)
            else:
                st.write("Please upload a PDF file.")
        else:
            st.warning("Please enter your OpenAI API Key to proceed.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        traceback.print_exc()

if __name__ == '__main__':
    process_pdf()
