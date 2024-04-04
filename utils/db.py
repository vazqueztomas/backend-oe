import os
import pymongo
import logging
from dotenv import load_dotenv

def get_database():
    load_dotenv()
    try:
        connection_string = os.getenv("MONGODB_ATLAS_CONNECTION_STRING")
        if not connection_string:
            raise ValueError("MongoDB Atlas connection string is not provided.")
        
        # Create a connection using MongoClient
        client = pymongo.MongoClient(connection_string)
        
        return client.get_database("users")
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB Atlas: {e}")
        raise

if __name__ == "__main__":
    dbname = get_database()
