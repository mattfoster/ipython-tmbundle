#!/usr/bin/python

"""
Twisted client for IPython Editor Servers
"""

from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
import sys

class EditorClient(LineReceiver):
    def connectionMade(self):
        self.sendLine(self.factory.begin)
        for line in self.factory.lines:
            self.sendLine(line)
        self.sendLine(self.factory.end)
        self.transport.loseConnection()

    def lineReceived(self, line):
        print "receive:", line

class EditorClientFactory(ClientFactory):
    protocol = EditorClient
    
    def __init__(self, lines, begin='#BEGINBLOCK', end='#ENDBLOCK'):
       self.lines = lines.split('\n')
       self.begin = begin
       self.end   = end

    def clientConnectionFailed(self, connector, reason):
        # print 'connection failed:', reason.getErrorMessage()
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        # print 'connection lost:', reason.getErrorMessage()
        reactor.stop()

def sendlines(socket, lines=''):
    """
    Connect to a specified `socket` and send the given `lines`.
    
    Assumes the socket exists.
    """
    try:
        factory = EditorClientFactory(lines)
        reactor.connectUNIX(socket, factory)
        reactor.run()
    except: 
        return False
    else:
        return True

if __name__ == '__main__':
    sendlines("print 'test!'")
