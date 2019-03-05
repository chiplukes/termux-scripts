# termux-scripts
scripts for setting up termux for tinkering with neovim, python, tasker, etc.

setup_termux.sh - installs basic stuff for using python and neovim

weather.py - receives a TIME variable string sent from tasker task, sends an intent back to another tasker task that reads the returned string.  Just a simple example of message passing from tasker to a python script in termux, then back to tasker.  Requires Termux:Task app installed.

Tasker Task to send TIME variable to termux:
 * Create new task, select action to be Plugin then Termux:Task
 * Executable:  weather.py (note: this should be in ~/.termux/tasker)
 * Arguments: %TIME
 * Save
 
Tasker Task to receive intent from Termux:
 * create new profile (Event -> System -> Intent Received )
 * Action: net.dinglish.tasker.wx
 * all other settings default.
 * create a new task
 * Action: Alert -> Say
 * Text: %wxstring
 * Link intent received profile to this new task 
 


