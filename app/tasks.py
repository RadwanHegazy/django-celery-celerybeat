from celery import shared_task




@shared_task( bind = True )
def CeleryTask (self) : 
    for i in range(10):print('task num : ', i)
    return "Task Completed from app 1"      