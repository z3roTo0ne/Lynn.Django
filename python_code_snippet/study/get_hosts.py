import torndb
import tornado.web
from tornado.options import options, define
from tornado.escape import json_encode
import tornado.httpserver
import tornado.ioloop
import tornado.log

define('server_port', default=8888, help=u"server port", type=int)
define('server_address', default="192.168.5.133", help=u"server address")
define('db_host', default="192.168.5.133:3307", help=u"mysql host")
define('db_user', default="root", help=u"mysql user")
define('db_password', default="root", help=u"mysql password")
define('db_database', default="yunwei", help=u"mysql database")


class ApiApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/get_host", GethostHandler),
        ]
        settings = dict(
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
        )
        super(ApiApplication, self).__init__(handlers, **settings)
        self.db = torndb.Connection(
            host=options.db_host, user=options.db_user,
            database=options.db_database, password=options.db_password
        )


class GethostHandler(tornado.web.RequestHandler):
    def __init__(self, application, request):
        self.db = application.db
        super(GethostHandler, self).__init__(application, request)
    # @property
    # def db(self):
    #     return self.application.db

    def get(self):
        # print self.request
        host = self.db.query("SELECT ip, hostname FROM host_host LIMIT 10")
        if not host:
            raise tornado.web.HTTPError(404)
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(host))
        self.finish()


if __name__ == "__main__":
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(ApiApplication())
    http_server.listen(options.server_port, address=options.server_address)
    print "server is running on: http://%s:%s" % (options.server_address, options.server_port)
    # tornado.ioloop.IOLoop.current().start()
    tornado.ioloop.IOLoop.instance().start()

