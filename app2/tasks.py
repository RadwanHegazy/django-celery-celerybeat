from celery import shared_task



@shared_task ( bind = True )
def App2Task (self) : 
    for i in range(10) : 
        print('app2 task : ' , i)

    return "Task run from app2 "