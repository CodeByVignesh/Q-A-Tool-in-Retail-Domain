from langchain_experimental.sql import SQLDatabaseChain

def query_db(db_connection, model):

    if db_connection is None:
        print("Database connection is not available.")
         return None
     
    try:
        db_chain = SQLDatabaseChain.from_llm(llm=model, db=db_connection, verbose=True)
        answer1 = db_chain.run("How many t-shirts do we have left for nike in extra small size and white color?")
        print(answer1)
        return answer1
    except Exception as e:
        print(f"Error querying the database: {e}")
        return None