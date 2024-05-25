import pandas as pd
from pymongo import MongoClient

# Read the CSV file into a DataFrame
csv_file = 'covid19_sample_data.csv'
df = pd.read_csv(csv_file)

# Convert DataFrame to a list of dictionaries
data = df.to_dict(orient='records')

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['covid19_database']
collection = db['covid19_data']

# Insert data into MongoDB collection
collection.insert_many(data)

print(f"Data from {csv_file} has been successfully inserted into MongoDB collection 'covid19_data' in 'covid19_database' database.")


    