
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, Activity, Leaderboard, Workout, OctoUser

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        OctoUser.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (Superheroes)
        users = [
            OctoUser.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            OctoUser.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel),
            OctoUser.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            OctoUser.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
        ]

        # Create Activities
        for user in users:
            Activity.objects.create(user=user, type='run', duration=30, distance=5)
            Activity.objects.create(user=user, type='cycle', duration=60, distance=20)

        # Create Workouts
        for user in users:
            Workout.objects.create(user=user, name='Morning Cardio', description='Cardio session', duration=45)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
