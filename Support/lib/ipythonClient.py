import os

from os.path import expanduser, join
from stat import ST_MODE, S_ISSOCK
from twisted_editor_client import sendlines

default_path=expanduser('~/.ipython/')

def list_sockets(path=default_path):
    """list the sockets in a given directory"""
    path = expanduser(path)
    files = os.listdir(path)

    # filter non-sockets
    def is_sock(f): 
        md = os.stat(join(path,f))[ST_MODE]
        return S_ISSOCK(md)

    return filter(is_sock, files)

def remove_sockets(path=default_path):
    """Remove all sockets in a given directory. 
    Potentially destructive!"""
    path = os.path.expanduser(path)
    socks = list_sockets(path)
    for sock in socks:
        os.remove(os.path.join(path, sock))

def determine_socket(path=default_path):
    """Determine the socket with which to connect."""
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
        
def find_server_then_connect(lines):
    """Determine which socket to connect to, then send `lines`
    
    Return `False` if there was a problem, otherwise `True`.
    """
    sock = determine_socket()
    if not sock:
    	return False
    else:
    	return sendlines(sock, lines)
    