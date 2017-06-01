import python_code_snippet.redis

__author__ = 'Administrator'


def redis_pub(content):
    conn = python_code_snippet.redis.Redis(host='192.168.5.133', port=6379)
    ps = conn.pubsub()
    ps.subscribe(['chat'])
    conn.publish('chat', content)
