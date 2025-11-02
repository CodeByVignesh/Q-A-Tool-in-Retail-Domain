import os
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain

#langchain.verbose = False
from langchain_experimental.sql import SQLDatabaseChain

from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("PaLM_API_KEY")

def get_model():
    try:
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-liter")

        def check_model():
            try:
                response = model.invoke("Why do parrots have colorful feathers?")
                print(response)
            except Exception as e:
                print(f"Error occurred: {e}")
                raise ConnectionError("Model invocation failed.")
        
        check_model()
        return model
    except Exception as e:
        print(f"Failed to initialize model: {e}")
        return None
