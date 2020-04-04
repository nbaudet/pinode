""" Declare some test classes """
from celery import Celery
from pinode.settings import RABBITMQ_USER, RABBITMQ_PASSWORD

BROKER = 'pyamqp://' + RABBITMQ_USER + ':' + RABBITMQ_PASSWORD + '@localhost//'
APP = Celery('tasks', broker=BROKER)

@APP.task
def add(first, second):
    """Test task"""
    return first + second
