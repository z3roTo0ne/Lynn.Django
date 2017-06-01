#! encoding:utf8
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import os
import redis
import threading

LISTENERS = []

REDIS_HOST = os.environ.get('REDIS_HOST', '192.168.5.133')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
TASK_CHANNEL = 'task_flow'
TORNADO_RUN_IP = os.environ.get('TORNADO_RUN_IP', '192.168.5.133')
TORNADO_RUN_PORT = os.environ.get('TORNADO_RUN_PORT', 1234)

'''
def redis_sub(channel):
    conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    ps = conn.pubsub()
    print channel
    ps.subscribe([channel])
    for item in ps.listen():
        for element in LISTENERS:
            if item['type'] == 'message':
                element.write_message(item['data'])
'''

class SocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        print ">>> new connection >>>"
        LISTENERS.append(self)

    def on_message(self, message):
        channel = message
        conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        ps = conn.pubsub()
        ps.subscribe([channel])
        for item in ps.listen():
            if item['type'] == 'message':
                self.write_message(item['data'])
                print "[%s] >>>\n--\t%s" % (channel, item['data'])

    def on_close(self):
        print "connection closed!"

application = tornado.web.Application([
    (r'/ws', SocketHandler),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(TORNADO_RUN_PORT, TORNADO_RUN_IP)
    print 'Tornado websocket server is running ...'
    tornado.ioloop.IOLoop.instance().start()
