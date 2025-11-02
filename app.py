import streamlit as st
from db_connection import create_database_connection
from langchain_google import get_model
import time
from query_db import query_db_func

st.title("TeraFyne T-Shirts DataBase Q&A Assistant")

Question = st.text_input("Please enter your question here..")

# Empty placeholder for status updates
status_placeholder = st.empty()

# Add a button to submit the question
if st.button("Submit"):
    if not Question:
        status_placeholder.error("Please enter a question before submitting.")
    else:
        # Connect to DB
        db_connection = create_database_connection()
        if db_connection is not None:
            status_placeholder.success("Database connection established.")
            # Load the model
            model = get_model()
            if model is not None:
                status_placeholder.success("Model loaded successfully.")
                # Here you would add the logic to process the question and return an answer
                time.sleep(2)  # Simulate processing time
                status_placeholder.info("Processing your question...")

                # Import query_db here to avoid circular imports

                answer = query_db_func(db_connection, model, Question)
                if answer is not None:
                    status_placeholder.empty()  # Clear status messages
                    st.subheader("Answer:")
                    st.write(answer)
                else:
                    status_placeholder.error("Failed to get an answer from the database.\nPlease try again later.")

            else:
                status_placeholder.error("Failed to load the model.")
        else:
            status_placeholder.error("Failed to connect to the database.")




    







