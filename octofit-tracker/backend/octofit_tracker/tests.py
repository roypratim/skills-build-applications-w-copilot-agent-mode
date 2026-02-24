from django.test import TestCase

from .models import Team, Activity, Workout, Leaderboard, OctoUser

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = OctoUser.objects.create_user(username='testuser', password='testpass', email='testuser@example.com', team=self.team)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user_team(self):
        self.assertEqual(self.user.team, self.team)

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user, type='run', duration=30, distance=5)
        self.assertEqual(activity.user, self.user)
        self.assertEqual(activity.type, 'run')

    def test_workout_creation(self):
        workout = Workout.objects.create(user=self.user, name='Test Workout', description='desc', duration=45)
        self.assertEqual(workout.user, self.user)
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team=self.team, points=50)
        self.assertEqual(leaderboard.team, self.team)
        self.assertEqual(leaderboard.points, 50)
