# mongodb_uploader.py
from pymongo import MongoClient

def upload_to_mongodb(data, db_name='log_data', collection_name='user_history'):
    try:
        client = MongoClient('mongodb+srv://rohithsmir1236:neDEoC7PBYr8cSeY@cluster0.itrdhnw.mongodb.net/')
        db = client[db_name]
        collection = db[collection_name]
        
        if data:
            collection.insert_many(data)
            print(f"✅ {len(data)} records uploaded to MongoDB collection '{collection_name}'.")
        else:
            print("⚠️ No data to upload.")
    except Exception as e:
        print("❌ Failed to upload data to MongoDB.")
        print("Error:", e)
