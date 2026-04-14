from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        user = User.objects.create(username='testuser')
        activity = Activity.objects.create(user=user, type='run', duration=30)
        self.assertEqual(str(activity), 'testuser - run')

    def test_leaderboard_creation(self):
        user = User.objects.create(username='testuser')
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(str(leaderboard), 'testuser - 100')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc')
        self.assertEqual(str(workout), 'Test Workout')
