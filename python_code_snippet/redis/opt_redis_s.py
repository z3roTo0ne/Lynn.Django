import python_code_snippet.redis

__author__ = 'Administrator'


def redis_sub():
    conn = python_code_snippet.redis.Redis(host='192.168.5.133', port=6379)
    ps = conn.pubsub()
    ps.subscribe(['chat'])
    for item in ps.listen():
        if item['type'] == 'message':
            print item['data']

redis_sub()
