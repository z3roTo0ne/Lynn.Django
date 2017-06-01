import zerorpc

class HelloRpc(object):
    def hello(self, name):
        print("hello, {}".format(name))


s = zerorpc.Server(HelloRpc())
s.bind("tcp://192.168.226.129:1234")
s.run()
