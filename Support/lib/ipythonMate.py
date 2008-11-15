#!/usr/bin/env python
# coding: utf-8
# Interact with Terminal.app using applescript

import os

# Applescript functions:

def run_in_terminal(text, proc_name='Python', app_name='Terminal', command='ipython'):
  """run the supplied `text` in a terminal (or supplied `app_name`)"""
  cmd = """osascript <<- APPLESCRIPT
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

def notify_with_growl(title, description):
    cmd = """osascript <<- APPLESCRIPT
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
  

  
