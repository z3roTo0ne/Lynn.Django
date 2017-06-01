from celery_worker import *

#taskA.apply_async((1, 2))

taskA.delay(1,2)