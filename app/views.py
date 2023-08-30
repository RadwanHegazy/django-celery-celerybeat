from django.shortcuts import HttpResponse
from . import tasks


def home (request) : 
    tasks.CeleryTask.delay()
    return HttpResponse('Done')