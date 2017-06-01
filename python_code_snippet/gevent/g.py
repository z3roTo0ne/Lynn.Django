# coding=utf-8
import gevent.monkey
import requests
gevent.monkey.patch_socket()
import gevent
import simplejson as json

def fetch(pid):
    response = requests.get('http://date.jsontest.com/')
    result = response.content
    json_result = json.loads(result)
    datetime = json_result['time']

    print('Process %s: %s' % (pid, datetime))
    return json_result['']

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()