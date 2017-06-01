import tornado.httpserver
import tornado.ioloop
from tornado.web import RequestHandler, Application
TORNADO_RUN_IP = "192.168.5.133"
TORNADO_RUN_PORT = 8195


class TestHandler(RequestHandler):
    def get(self):
        self.write("hello world\n")


application = Application([
    (r'/', TestHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(TORNADO_RUN_PORT, TORNADO_RUN_IP)
    print 'Tornado web socket server is running ...'
    tornado.ioloop.IOLoop.instance().start()
