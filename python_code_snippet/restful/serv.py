import os
import tornado
import tornado.web
import tornado.gen
import json
from tornado import httpserver
from tornado import ioloop
from tornado.options import define, options
from tornado_mysql import pools
from collections import defaultdict

define('listen_port', default=8008, help='server listen port', type=int)
define('listen_address', default='0.0.0.0', help='server listen address', type=str)


define('db_host', default='192.168.208.128', help='api database host', type=str)
define('db_port', default=3306, help='api database port', type=int)
define('db_user', default='db_api', help='api database user', type=str)
define('db_password', default='db_api', help='api database password', type=str)
define('db_name', default='db_api', help='api database name', type=str)

mysql_conn = dict(host=options.db_host, port=options.db_port, user=options.db_user, db=options.db_name, password=options.db_password)
MYSQL_POOL = pools.Pool(mysql_conn, max_idle_connections=5, max_open_connections=10)


class BookListHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        cursor = yield MYSQL_POOL.execute('SELECT * FROM book')
        data = {'book_list': {}}
        for row in cursor:
            book_name = row[1]
            book_id = row[0]
            book = {book_id: book_name}
            data['book_list'].update(book)
        data['version'] = '1.0'
        self.write(data)
        self.finish()


class BookDetailHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, book_id):
            cursor = yield MYSQL_POOL.execute('SELECT * FROM book where book_id={}'.format(book_id))
            data = {'book_info':{}}
            for row in cursor:
                book_id = row[0]
                book_name = row[1]
                book_author = row[2]
                book_country = row[3]
                book_publisher = row[4]
                book_info = dict(
                    book_id=book_id,
                    book_name=book_name,
                    book_author=book_author,
                    book_country=book_country,
                    book_publisher=book_publisher )
                data['book_info'].update(book_info)
            data['version'] = '1.0'
            self.write(data)
            self.finish()

    def post(self, *args, **kwargs):
        print self.get_body_argument('book_name')
        # b_id = self.get_argument('book_id')
        # b_name = self.get_argument('book_name')
        # b_author = self.get_argument('book_author')
        # b_country = self.get_argument('book_country')
        # # b_publisher = self.get_argument('book_publisher')
        # self.get(b_id)
        # self.write(bname)


class Application(tornado.web.Application):
    def __init__(self):
        project_dir = os.getcwd()
        handlers = [
            (r'/api/v1/items', BookListHandler),
            (r'/api/v1/items/(\d+$)', BookDetailHandler),
            # (r'/ap1/v1/items/(\d+)/(edit)$', ItemHandler),
            (r"/all_books", BookHandler),
            (r"/all_category/", CategoryHandler),
        ]

        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings)


class BookHandler(object):
    pass

class CategoryHandler(object):
    pass


if __name__ == '__main__':
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    print "server running on {}:{}  ...".format(options.listen_address, options.listen_port)
    http_server.listen(options.listen_port, options.listen_address)
    tornado.ioloop.IOLoop.instance().start()