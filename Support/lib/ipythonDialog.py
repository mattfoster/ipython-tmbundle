import os
import sys

tm_support_path = os.environ['TM_SUPPORT_PATH'] + '/lib'
if tm_support_path not in sys.path:
    sys.path.insert(0, tm_support_path)

from tm_helpers import to_plist, from_plist

dialog  = os.environ.get('DIALOG')

def get_confirmation(title_text='', body_text='' ):
    """Use dialog2 to ask for confirmation 
    
    Returns `True` to indicate confirmation. 
    Returns `None` to indicate an error.
    """
    dtype   = 'alert'
    style   = '--alertStyle warning'
    title   = "--title '%s'" % title_text or 'Confirm file deletion'
    body    = "--body '%s'" % body_text or 'Confirm file deletion:'
    buttons = "--button1 Delete --button2 Cancel"
    args    = ' '.join(["'%s'" % dialog, dtype, style, title, body, buttons])
    output  = os.popen(args, 'r').read()
    result  = from_plist(output)
    
    if not 'buttonClicked' in result:
        return None
    
    return int(result['buttonClicked']) == 0

def html_tooltip(text=''):
    """Show an HTML tooltip using tm_dialog2
    """
    
    # Based on PHP bundle's CSS
    css = """ 
      <style type="text/css" media="screen">
          p {
              margin: 0;
              font-family: Monaco;
              font-size: 8pt;
          }
          p span {
              color: #00008B;
          }
          p i {
              color: #666;
          }
      </style>
      <p>%s</p>
    """ % text or 'tooltip!'
    
    dtype = 'tooltip'
    opts  = '--html "%s"' % css
    args  = ' '.join(["'%s'" % dialog, dtype, opts])
    os.system(args)

# Old dialog version:
def _get_confirmation():
    """get confirmation"""

    support_path     = os.environ.get('TM_SUPPORT_PATH')
    cocoa_dialog     = os.path.join(support_path, "bin/CocoaDialog.app/Contents/MacOS/CocoaDialog")

    dtype            = "msgbox"
    text             = '--text "This command will remove all sockets from .ipythonrc"'
    icon             = '--icon "x"' 
    informative_text = '--informative-text "There are files in the socket directory. They will be removed if you continue."' 
    buttons          = '--button1 "Cancel Deletion" --button2 "Delete all"'

    # Join args to build command.
    args = ' '.join(["'%s'" % cocoa_dialog, dtype, text, icon, informative_text, buttons])

    output = os.popen(args, 'r').read()

    if int(output) == 2:
        return True
    else: 
        return False

