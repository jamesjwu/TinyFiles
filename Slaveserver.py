"""
TinyFiles- A simple, tiny, distributed, replicated file system

Slave file server for writing files
"""
from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
from filerequest_pb2 import FileRequest, FileResponse
import os



class TinyFileSlave(Protocol):
    """Slave server - currently just echos the result onto console."""
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

        result = FileResponse()
        if info.request_type == FileRequest.WRITE:
            try:
                # write to the file
                f = open("datastore/" + info.filename, 'w+')
            except IOError, e:
                print "File IO Error:", e
                return d
            f.write(info.contents)
            f.close()
            result.success = True

        elif info.request_type == FileRequest.READ:
            try:
                f = open("datastore/" + info.filename, 'r')
            except IOError, e:
                print "Error: File does not exist"
                result.success = False
                result.contents = "Error: File does not exist"
                self.transport.write(result.SerializeToString())
                return

            result.success = True
            result.contents = f.read()
            f.close()

        elif info.request_type == FileRequest.APPEND:
            try:
                f = open("datastore/" + info.filename, 'a+ ')
            except IOError, e:
                print "Error: File does not exist"
                result.success = False
                result.contents = "Error: File does not exist"
                self.transport.write(result.SerializeToString())
                return
            
            f.write(info.contents)
            f.close()
            result.success = True

        elif info.request_type == FileRequest.DELETE:
            try:
                os.remove("datastore/" + info.filename)
            except IOError, e:
                print "Error, no such file to delete"
                result.success = False
                result.contents = "Error: File does not exist"
                self.transport.write(result.SerializeToString())
                return

            result.success = True

        self.transport.write(result.SerializeToString())

factory = Factory()
factory.protocol = TinyFileSlave
reactor.listenTCP(1112, factory)
print "TinyFile server started"
reactor.run()

