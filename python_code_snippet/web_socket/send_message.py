import redis
import os
import time

REDIS_HOST = os.environ.get('REDIS_HOST', '192.168.5.133')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_DB = 0

conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
conn.publish("task_flow", 'fuck you')

i = 1
while i <= 10:
    i += 1
    conn.publish("task_flow", 'fuck you %d times' % i)
    time.sleep(3)
