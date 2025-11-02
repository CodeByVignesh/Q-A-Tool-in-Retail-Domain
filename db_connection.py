
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_community.utilities import SQLDatabase

def create_database_connection():
    try:
        db_connection = SQLDatabase.from_uri(
            f"mysql+pymysql://{os.getenv('db_user_name')}:{os.getenv('db_password')}@{os.getenv('db_host')}/{os.getenv('db_name')}",
            sample_rows_in_table_info=3,
        )

        print(db_connection.table_info)
        return db_connection
    except Exception as e:
        print(f"Error creating database connection: {e}")
        db_connection = None
        return db_connection
