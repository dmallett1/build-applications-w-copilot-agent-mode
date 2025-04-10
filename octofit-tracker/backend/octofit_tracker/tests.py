from django.test import TestCase
from .models import User, Team, Activities, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="password123")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team A", members=["user1", "user2"])
        self.assertEqual(team.name, "Team A")

class ActivitiesModelTest(TestCase):
    def test_activities_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="password123")
        activities = Activities.objects.create(user=user, type="Running", duration=30)
        self.assertEqual(activities.type, "Running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        team = Team.objects.create(name="Team A", members=["user1", "user2"])
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Workout A", description="Test workout description")
        self.assertEqual(workout.name, "Workout A")