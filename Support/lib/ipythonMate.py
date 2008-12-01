#!/usr/bin/env python
# coding: utf-8
# Interact with Terminal.app using applescript

import os

def selection_or_line():
    """Return selected text, the current line or None if there's a problme"""

    try:
        text=os.environ['TM_SELECTED_TEXT']
    except KeyError:
        text=os.environ.get('TM_CURRENT_LINE')

    return text


# Utility functions:
def get_ipython_cmd():
    """docstring for get_ipython_cmd"""
    try:
    	cmd=os.environ['TM_IPYTHON']
    except KeyError:
    	cmd='ipython'
    
    return cmd

# Applescript functions:

def run_in_terminal(text, proc_name='Python', app_name='Terminal', command='ipython'):
  """run the supplied `text` in a terminal (or supplied `app_name`)"""
  cmd = """osascript 2>&1>/dev/null<<- APPLESCRIPT
          tell application "%s"
                  set currentTab to (selected tab of (get first window))
                  set tabProcs to processes of currentTab
                  set theProc to (end of tabProcs)
                  if theProc is not "%s" then
                          set currentTab to (do script "%s")
                  end if

                  do script "%s" in currentTab
          end tell 
  APPLESCRIPT""" % (app_name, proc_name, command, text)
  os.system(cmd)


def open_in_terminal(text, app_name='Terminal', command='ipython'):
    """Slightly different method (from Octave.app)"""
    cmd="""osascript 2>&1>/dev/null <<-EOF
        tell application "System Events" to set ProcessList to get name of every process
        tell application "%s" 
          activate
          if ProcessList contains "%s" then
            do script "%s"
          else
            do script "%s" in front window
          end if
          do script "%s" in front window
        end tell
    EOF""" % (app_name, app_name, command, command, text)
    os.system(cmd)
  
def notify_with_growl(title, description):
    cmd = """osascript 2>&1>/dev/null<<- APPLESCRIPT
    tell application "GrowlHelperApp"
    	-- Make a list of all the notification types 
    	-- that this script will ever send:
    	set the allNotificationsList to ¬
    		{"ipythonMate"}

    	-- Make a list of the notifications 
    	-- that will be enabled by default.      
    	-- Those not enabled by default can be enabled later 
    	-- in the 'Applications' tab of the growl prefpane.
    	set the enabledNotificationsList to ¬
    		{"ipythonMate"}

    	-- Register our script with growl.
    	-- You can optionally (as here) set a default icon 
    	-- for this script's notifications.
    	register as application ¬
    		"TextMate" all notifications allNotificationsList ¬
    		default notifications enabledNotificationsList ¬
    		icon of application "TextMate"

    	--	Send a Notification...
    	notify with name ¬
    		"ipythonMate" title ¬
    		"%s" description ¬
    		"%s" application name "TextMate"
    end tell

    APPLESCRIPT""" % (title, description)
    os.system(cmd)
    
if __name__ == '__main__':
  # run_in_terminal("ls")
  notify_with_growl("Ran IPython Script", "test")
  

  
