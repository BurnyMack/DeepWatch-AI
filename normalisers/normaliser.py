import requests
import json
from pymongo import MongoClient

# Replace 'your_api_endpoint' with the actual API endpoint you want to fetch data from
api_url = 'your_api_endpoint'

# Connect to your MongoDB database (replace with your MongoDB connection details)
client = MongoClient('mongodb://username:password@localhost:27017/')
db = client['your_database_name']
collection = db['your_collection_name']

# Send a GET request to the API
response = requests.get(api_url, stream=True)

if response.status_code == 200:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            # Process the chunk of data (assuming it's JSON)
            data = chunk.decode('utf-8')
            try:
                # Parse the JSON data
                parsed_data = json.loads(data)
                # Normalize the JSON if needed
                # For example, you can convert keys to lowercase or perform other transformations
                normalized_data = {k.lower(): v for k, v in parsed_data.items()}
                # Insert the normalized data into MongoDB
                collection.insert_one(normalized_data)
            except json.JSONDecodeError:
                print("Failed to parse JSON data")
else:
    print(f"Failed to retrieve data from the API. Status code: {response.status_code}")

# Close the MongoDB connection
client.close()