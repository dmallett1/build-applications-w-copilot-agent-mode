from pymongo import MongoClient
from django.conf import settings

def remove_duplicates():
    client = MongoClient()
    db = client[settings.DATABASES['default']['NAME']]

    collections = ['users', 'teams', 'activity', 'leaderboard', 'workouts']

    for collection_name in collections:
        collection = db[collection_name]
        seen = set()
        duplicates = []

        for document in collection.find():
            identifier = tuple(document.items())  # Create a unique identifier for each document
            if identifier in seen:
                duplicates.append(document['_id'])
            else:
                seen.add(identifier)

        if duplicates:
            collection.delete_many({'_id': {'$in': duplicates}})
            print(f"Removed {len(duplicates)} duplicates from {collection_name}.")
        else:
            print(f"No duplicates found in {collection_name}.")

def drop_and_recreate_database():
    client = MongoClient()
    db_name = settings.DATABASES['default']['NAME']

    # Drop the database
    client.drop_database(db_name)
    print(f"Database '{db_name}' has been dropped.")

    # Recreate the database
    db = client[db_name]
    print(f"Database '{db_name}' has been recreated.")

if __name__ == "__main__":
    drop_and_recreate_database()