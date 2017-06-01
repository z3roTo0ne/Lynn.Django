# coding=utf-8
import logging
import os, sys
from logging import config as logging_config
import json
from functools import wraps

DEBUG=False

def setup_logging(default_path='logging.json', default_level=logging.DEBUG, env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging_config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def log_func(func):
    @wraps(func)
    def _deco(*args, **kwargs):
        content = "function {}() was called. received arguments: {}".format(func.__name__, (args, kwargs))
        logger.debug(content)
        return func(*args, **kwargs)

    return _deco

@log_func
def hello(name):
    print "hello {}".format(name)
    logger.info('hello error')


if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger('hotpot.app.verbose') if DEBUG else logging.getLogger('hotpot.app')
    hello("chenlin")

