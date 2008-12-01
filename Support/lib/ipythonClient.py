import socket
import os

from os.path import expanduser, join
from stat import ST_MODE, S_ISSOCK

# Adapted from ipy.vim (vim / ipython server)
# In TextMate, we can't rely on environment variables set in a terminal

IPYSERVER = None

def check_server():
    global IPYSERVER
    if IPYSERVER:
        return True
    else:
        return False

# connect to the ipython server, if we need to
def connect(server):
    """Connect to the server given in the string `server` """
    # print "Connecting to", expanduser(server)
    global IPYSERVER
    if check_server():
        return
    try:
        IPYSERVER = socket.socket(socket.AF_UNIX)
        IPYSERVER.connect(expanduser(server))
    except:
        IPYSERVER = None
                
    if IPYSERVER != None:
        return True
    else:
        return False

def disconnect():
    if IPYSERVER:
        IPYSERVER.close()

def send(cmd):
    x = 0
    while True:
        x += IPYSERVER.send(cmd)
        if x < len(cmd):
            cmd = cmd[x:]
        else:
            break

def run_this_file(filename):
    if check_server():
        send('run %s' % (filename))
    else:
        raise Exception, "Not connected to an IPython server"

def list_sockets(path='~/.ipython/'):
    """list the sockets in a given directory"""
    path = expanduser(path)
    files = os.listdir(path)

    # filter non-sockets
    def is_sock(f): 
        md = os.stat(join(path,f))[ST_MODE]
        return S_ISSOCK(md)

    return filter(is_sock, files)

def remove_sockets(path='~/.ipython'):
    """Remove all sockets in a given directory. 
    Potentially destructive!"""
    path = os.path.expanduser(path)
    socks = list_sockets(path)
    for sock in socks:
        os.remove(os.path.join(path, sock))

def determine_socket(path='~/.ipython'):
    """Find out which socket to connect to"""
    sockets = list_sockets(path)

    if not len(sockets):
        return None

    if len(sockets) == 1:
        return os.path.join(path, sockets[0])
    
    try:
        import dialog
        # If we aren't running from within TM use the first socket found.
    except ImportError:
        sock = sockets[0]
    else:
        sock = dialog.menu(sockets)            

    return os.path.join(path, sock)
        
def find_server_then_connect():
    """Find and connect to a socket server"""
    sock = determine_socket()
    if sock == None:
    	connected = False
    else:
    	connected = connect(sock)
    return connected
    