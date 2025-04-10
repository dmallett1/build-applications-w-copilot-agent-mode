from pymongo import MongoClient

def initialize_database():
    # Connect to MongoDB
    client = MongoClient()

    # Specify the database name
    db_name = "octofit_db"
    db = client[db_name]

    # Drop the database if it already exists
    client.drop_database(db_name)
    print(f"Database '{db_name}' dropped and reinitialized.")

    # Create collections and indexes
    db.users.create_index("email", unique=True)
    print("Created 'users' collection with unique index on 'email'.")

    db.teams.create_index("name", unique=True)
    print("Created 'teams' collection with unique index on 'name'.")

    db.activities.create_index("user_id")
    print("Created 'activities' collection with index on 'user_id'.")

    db.leaderboard.create_index("team_id")
    print("Created 'leaderboard' collection with index on 'team_id'.")

    db.workouts.create_index("name", unique=True)
    print("Created 'workouts' collection with unique index on 'name'.")

    # List collections in the database
    collections = db.list_collection_names()
    print("Collections in the database:", collections)

if __name__ == "__main__":
    initialize_database()
