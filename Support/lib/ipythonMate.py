#!/usr/bin/env python
# Interact with Terminal.app using applescript

import os

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
  
if __name__ == '__main__':
  run_in_terminal("ls")
  

  
