from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*agrs, **kwargs):
        print func.__name__ + 'was called'
        return func(*agrs, **kwargs)

    return with_logging



@logit
def add(x):
    return 2*x

if __name__ == '__main__':
   add(2)



