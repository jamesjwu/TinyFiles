"""
TinyFiles- A simple, tiny, distributed, replicated file system

Master file server that generates requests.
"""
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from filerequest_pb2 import FileRequest, FileResponse
import time

class Sender(Protocol):
    def sendMessage(self, filename, request_type, contents=""):
        new_request = FileRequest()
        new_request.filename = filename
        new_request.request_type = request_type
        new_request.contents = contents
        
        self.transport.write(new_request.SerializeToString())

    def connectionMade(self):
    	print "Connection made"
        try:
            f = open("test.txt", 'r')            
        except IOError:
            print "Invalid filename."
            return

        self.sendMessage("test.txt", FileRequest.WRITE, f.read())


        f.close()

    def dataReceived(self, data):
        result = FileResponse()
        result.ParseFromString(data)
        print result.success
        if(result.contents):
            print result.contents


point = TCP4ClientEndpoint(reactor, "localhost", 1112)
d = connectProtocol(point, Sender())

reactor.run()