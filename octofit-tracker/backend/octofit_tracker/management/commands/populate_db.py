from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from octofit_tracker.models import Team, Activity, Leaderboard, Workout
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Users
        tony = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='pass', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='hulk', email='hulk@marvel.com', password='pass', first_name='Bruce', last_name='Banner', team=marvel)
        clark = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent', team=dc)
        bruce_dc = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne', team=dc)

        # Workouts
        w1 = Workout.objects.create(name='Pushups', description='Pushups workout')
        w2 = Workout.objects.create(name='Running', description='Running workout')
        w3 = Workout.objects.create(name='Swimming', description='Swimming workout')

        # Activities
        Activity.objects.create(user=tony, workout=w1, duration=30, calories=200)
        Activity.objects.create(user=steve, workout=w2, duration=45, calories=350)
        Activity.objects.create(user=clark, workout=w3, duration=60, calories=500)

        # Leaderboard
        Leaderboard.objects.create(user=tony, points=1000)
        Leaderboard.objects.create(user=steve, points=900)
        Leaderboard.objects.create(user=clark, points=1100)


        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

# Models for reference (should be in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100)
#
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
#     duration = models.IntegerField()
#     calories = models.IntegerField()
#
# class Leaderboard(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     points = models.IntegerField()
