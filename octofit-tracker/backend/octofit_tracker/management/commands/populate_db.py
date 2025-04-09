from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data using MongoDB client
        client = MongoClient()
        db = client[settings.DATABASES['default']['NAME']]
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', password='password123'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', password='password123'),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', password='password123'),
            User(email='crashoverride@hmhigh.edu', name='Natasha Romanoff', password='password123'),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', password='password123'),
        ]
        for user in users:
            user.save()

        # Create teams
        teams = [
            Team(name='Blue Team', members=[]),
            Team(name='Gold Team', members=[]),
        ]
        for team in teams:
            team.save()

        # Add members to teams
        teams[0].members = [str(users[0].id), str(users[1].id)]
        teams[1].members = [str(users[2].id), str(users[3].id), str(users[4].id)]
        for team in teams:
            team.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60),
            Activity(user=users[1], type='Crossfit', duration=120),
            Activity(user=users[2], type='Running', duration=90),
            Activity(user=users[3], type='Strength', duration=30),
            Activity(user=users[4], type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team={"id": str(teams[0].id), "name": teams[0].name, "members": teams[0].members}, score=100),
            Leaderboard(team={"id": str(teams[1].id), "name": teams[1].name, "members": teams[1].members}, score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))