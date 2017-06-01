import eventlet
from eventlet import wsgi
from eventlet import websocket



# import gevent
# from gevent import wsgi, pool
#
#
# def app(environ, start_response):
#     start_response("200 OK", [("Content-Type","text/plain")])
#     return "Hello World\n"
#
# if __name__ == "__main__":
#     print "server is running on http://192.168.5.133:8192/"
#     pool = gevent.pool.Pool()
#     server = wsgi.WSGIServer(("192.168.5.133", 8192), app, spawn=pool)
#     server.serve_forever()



@websocket.WebSocketWSGI
def hello_world(ws):
    ws.send("hello world")

wsgi.server(eventlet.listen(('192.168.5.133', 1234)), hello_world)
