# termux-scripts
scripts for setting up termux for tinkering with neovim, python, tasker, etc.

setup_termux.sh - installs basic stuff for using python and neovim

weather.py - receives a TIME variable string sent from tasker task, sends an intent back to another tasker task that reads the returned string.  Just a simple example of message passing from tasker to a python script in termux, then back to tasker.  TODO: document the tasker tasks for this here!

