import os
import streamlit as st
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone as PC
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

# Streamlit page setup
def process_pdf():
    try:
        # Streamlit page setup
        st.title("PDF Processing with AI")

        # Get OpenAI API key from user
        api_key = st.text_input("Enter your OpenAI API Key", type="password")
        if api_key:
            # Proceed if API key is entered
            uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], key="pdf_uploader")

            if uploaded_file is not None:
                # Create a temporary file to save the uploaded file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    # Write the uploaded file to the temporary file
                    tmp_file.write(uploaded_file.getvalue())
                    temp_pdf_path = tmp_file.name
                pinecone_index_name = 'rag-pdf-index'

                # Read the PDF from the uploaded file
                st.write('Loading document...')
                loader = PyPDFLoader(temp_pdf_path)
                data = loader.load()
                os.unlink(temp_pdf_path)  # Remove the temporary file after loading

                st.write(f'You have loaded a PDF with {len(data)} pages')
                # st.write(f'There are {len(data[0].page_content)} characters in your document')

                # Chunk data into smaller documents
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
                texts = text_splitter.split_documents(data)

                # st.write(f'You have split your document into {len(texts)} smaller documents')

                # Create embeddings and index from your documents
                st.write('Creating embeddings and index...')
                
                embeddings = OpenAIEmbeddings(api_key=api_key)  # Use the provided API key
                docsearch = PC.from_texts(
                    [t.page_content for t in texts], embeddings, index_name=pinecone_index_name)

                st.success('Done!')

                st.title('Document Answering with Langchain and Pinecone')
                usr_input = st.text_input('What is your question?')

                # Set OpenAI LLM and embeddings
                llm_chat = ChatOpenAI(temperature=0.9, max_tokens=150,
                                    model='gpt-3.5-turbo-0613', api_key=api_key)

                embeddings = OpenAIEmbeddings(api_key=api_key)

                # Set Pinecone index
                docsearch = PC.from_existing_index(
                    index_name=pinecone_index_name, embedding=embeddings)

                # Create chain
                chain = load_qa_chain(llm_chat)

                # Check Streamlit input
                if usr_input:
                    # Generate LLM response
                    try:
                        search = docsearch.similarity_search(usr_input)
                        response = chain.run(input_documents=search, question=usr_input)
                        print('Response:', response)
                        st.write(response)
                    except Exception as e:
                        st.write('It looks like you entered an invalid prompt. Please try again.')
                        print(e)

                    with st.expander('Document Similarity Search'):

                        # Display results
                        search = docsearch.similarity_search(usr_input)
                        print('Search results:', search)
                        st.write(search)
            else:
                st.write("Please upload a PDF file.")
        else:
            st.warning("Please enter your OpenAI API Key to proceed.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    process_pdf()
