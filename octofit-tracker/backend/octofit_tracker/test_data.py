# Test data for populating the database

test_users = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

test_teams = [
    {"name": "Blue Team"},
    {"name": "Gold Team"},
]

test_activities = [
    {"user_email": "thundergod@mhigh.edu", "type": "Cycling", "duration": 60},
    {"user_email": "metalgeek@mhigh.edu", "type": "Crossfit", "duration": 120},
    {"user_email": "zerocool@mhigh.edu", "type": "Running", "duration": 90},
    {"user_email": "crashoverride@hmhigh.edu", "type": "Strength", "duration": 30},
    {"user_email": "sleeptoken@mhigh.edu", "type": "Swimming", "duration": 75},
]

test_leaderboard = [
    {"team_name": "Blue Team", "score": 100},
    {"team_name": "Gold Team", "score": 90},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]
