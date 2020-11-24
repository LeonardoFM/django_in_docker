from celery import shared_task
from .models import Solver

from celery.decorators import periodic_task
from celery.schedules import crontab

@shared_task
def create_solver_object(name):
    Solver.objects.create(name=name)

@periodic_task(run_every=(crontab(minute='*/1')))
def run_create_objs():
    create_solver_object.delay(name='2020')