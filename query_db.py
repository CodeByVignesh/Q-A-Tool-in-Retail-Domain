from langchain_experimental.sql import SQLDatabaseChain

def query_db_func(db_connection, model, question):

    if db_connection is None:
        print("Database connection is not available.")
        return None
     
    try:
        db_chain = SQLDatabaseChain.from_llm(llm=model, db=db_connection, verbose=True)
        answer1 = db_chain.run(question)
        print(answer1)
        return answer1
    except Exception as e:
        print(f"Error querying the database: {e}")
        return None