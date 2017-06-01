from python_code_snippet.celery import Celery
from celery.bin import worker


app_celery = Celery()
app_celery.config_from_object("celeryconfig")


@app_celery.task
def taskA(x,y):
    return x + y 

if __name__ == "__main__":
    argv = [ 
        'worker',
        '--loglevel=INFO',
        ]   
    app_celery.worker_main(argv) 