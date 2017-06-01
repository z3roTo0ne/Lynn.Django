from tornado import httpserver
from tornado import web
from tornado import ioloop
import json


class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        print self.request
        remote_address = self.request.remote_ip
        remote_ip = self.request.headers.get("x-forwarded-for", "")
        real_ip = self.request.headers.get("x-real-ip", "")

        data = {
            "remote_address": remote_address,
            "x-forwarded-for": remote_ip,
            "x-real-ip": real_ip
        }
        return self.write(json.dumps(data, indent=4)+"\n")


application = web.Application([
    (r"/", MainPageHandler),
])

if __name__ == "__main__":
    IP = '192.168.226.128'
    PORT = 8081
    http_server = httpserver.HTTPServer(application)
    print "start server at {ip}:{port}".format(ip=IP, port=PORT)
    http_server.listen(PORT, IP)
    ioloop.IOLoop.current().start()