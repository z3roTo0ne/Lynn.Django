from kombu import Exchange,Queue


BROKER_URL = "redis://192.168.5.133:6379/0"
CELERY_RESULT_BACKEND = "redis://192.168.5.133:6379/0"
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']


CELERY_QUEUES = (
        Queue("default",Exchange("default"),routing_key="default"), 
        Queue("for_task_A",Exchange("for_task_A"),routing_key="task_a"),
        Queue("for_task_B",Exchange("for_task_B"),routing_key="task_b") 
)
    

CELERY_ROUTES = {
        'my_celery.taskA':{"queue":"for_task_A","routing_key":"task_a"},
        'my_celery.taskB':{"queue":"for_task_B","routing_key":"task_b"}
        }

CELERY_TIMEZONE = 'UTC'

CELERYBEAT_SCHEDULE = {
        'taskA_schedule' : {
                'task':'my_celery.taskA',
                'schedule':2,
                'args':(5,6)
    },

        'taskB_scheduler' : {
                'task':"my_celery.taskB",
                "schedule":5,
                "args":(10,20,30)
        },
}