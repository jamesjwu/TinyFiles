"""
TinyFiles- A simple, tiny, distributed, replicated file system

Slave file server for writing files
"""
from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
from filerequest_pb2 import FileRequest



class TinyFileSlave(Protocol):
	"""Slave server — currently just echos the result onto console."""
    def connectionMade(self):
        print "Master server connected"
 
    def connectionLost(self, reason):
        print "Master server disconnected"

    def dataReceived(self, data):
    	"""We've gotten a request. It comes in a protocol buffer form."""
        # get the request protocol buffer
        print "Received data"
        info = FileRequest()
        info.ParseFromString(data)
        print "Filename:", info.filename
        print "Request type:", info.request_type
        print "File contents:", info.contents





factory = Factory()
factory.users = {}
factory.protocol = TinyFileSlave

reactor.listenTCP(1112, factory)
print "TinyFile server started"
reactor.run()

