import streamlit as st
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS

# Define the embedding function
huggingface_embeddings = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",  
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

# Define the vector store
vectorstore = FAISS.load_local("faiss_index", embeddings=huggingface_embeddings, allow_dangerous_deserialization=True)

# Define the chat model
chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    groq_api_key="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",
)

# Define the prompt template
PROMPT_TEMPLATE = """Virtual Assistant: You're in a bustling virtual marketplace where customers seek assistance. Your task is to help customers by providing accurate answers to their inquiries using the given information.

Context:
{context}

Customer's Question:
{question}
"""

prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["context", "question"])

# Define the retrievalQA
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})  # Assuming you have defined a retriever in the vector store

retrievalQA = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

# Streamlit app
st.title("Virtual Assistant Query System")

# Input query
query = st.text_input("Enter your query:")

# Button to submit query
if st.button("Submit"):
    if query:
        # Call the QA chain with the query
        result = retrievalQA.invoke({"query": query})
        st.write(result['result'])
        print(result['result'])
    else:
        st.write("Please enter a query.")
