from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()

# Specify the database name
db_name = "octofit_db"

# Drop the database
client.drop_database(db_name)

print(f"Database '{db_name}' has been removed successfully.")
