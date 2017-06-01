# coding=utf-8
from SimpleXMLRPCServer import SimpleXMLRPCServer
def is_even(n):
    return n%2 == 0
server = SimpleXMLRPCServer(("localhost", 8000))#确定URL和端口
print "Listening on port 8000..."
server.register_function(is_even, "is_even") #注册is_even函数
server.serve_forever()#启动服务器,并使其对这个连接可用

