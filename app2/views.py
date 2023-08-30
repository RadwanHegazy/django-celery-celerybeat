from django.shortcuts import HttpResponse
from .tasks import App2Task


def home (request) : 
    App2Task.delay()

    return HttpResponse('App 2 task in running..')