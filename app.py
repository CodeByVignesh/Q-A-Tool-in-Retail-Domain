import streamlit as st
from db_connection import create_database_connection
from langchain_google import get_model

st.title("DataBase Q&A Assistant")

Question = st.text_input("Please enter your question here..")

# Add a button to submit the question
if st.button("Submit"):
    # Here you would add the logic to process the question and return an answer
    st.info("Processing your question...")

    # Connect to DB
    db_connection = create_database_connection()
    if db_connection is not None:
        st.success("Database connection established.")
    else:
        st.error("Failed to connect to the database.")  
    
    # Load the model
    model = get_model()
    if model is not None:
        st.success("Model loaded successfully.")
    else:
        st.error("Failed to load the model.")


    







