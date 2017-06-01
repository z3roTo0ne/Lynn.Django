import zerorpc
c = zerorpc.Client()
c.connect("tcp://192.168.226.129:1234")
print c.hello("chen lin")