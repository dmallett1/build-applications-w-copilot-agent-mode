from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(id=ObjectId(), name='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(id=ObjectId(), name='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(id=ObjectId(), name='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(id=ObjectId(), name='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User(id=ObjectId(), name='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(id=ObjectId(), name='Blue Team', members=[]),
            Team(id=ObjectId(), name='Gold Team', members=[]),
        ]
        Team.objects.bulk_create(teams)

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