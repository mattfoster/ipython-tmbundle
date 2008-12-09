import socket
import ipythonClient as ipc

import nose
from nose import SkipTest
from nose.tools import with_setup

class TestCheckServer:
    def test_check_unset_server(self):
        """This just checks that IPYSERVER is unset. 
        We can assume it's something sensible, since it shouldn't be set 
        manually"""
        assert ipc.check_server() == False, "No server setup returns False"
        
    def test_check_unset_server(self):
        """This just checks that IPYSERVER is set. 
        We can assume it's something sensible, since it shouldn't be set 
        manually"""
        ipc.IPYSERVER = 'test'
        assert ipc.check_server() == True, "With server returns true"
        
class TestConnect:
    def test_connect(self):
        raise SkipTest # TODO: implement your test here

class TestDisconnect:
    def test_disconnect(self):
        raise SkipTest # TODO: implement your test here

class TestSend:
    def test_send(self):
        raise SkipTest # TODO: implement your test here

class TestRunThisFile:
    def test_run_this_file(self):
        raise SkipTest # TODO: implement your test here

class TestSockets:    
    socks = ['sock_1', 'sock_2']
    
    def setUp(self):
        """create some sockets in to list and delete"""
        for sock in self.socks:
            print 'creating sock'
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            try:
                s.bind(sock)
            except: # What exception is it?
                pass
            
    def test_list_sockets(self):
        assert ipc.list_sockets('.') == self.socks, "Check we list all the sockets"

    # This will only work if we haven't already deleted them! 
    def test_determine_socket(self):
        import os.path
        assert ipc.determine_socket('.') == os.path.join('.', self.socks[0]), "check we just pick the first"

    def test_remove_sockets(self):
          import os
          ipc.remove_sockets('.')
          for sock in self.socks:
              assert os.path.exists(sock) == False, "Check we've removed the socks"
  

if __name__ == '__main__':
    nose.run()