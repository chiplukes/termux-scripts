# use f-droid to install the following
 * Termux Terminal emulator with packages
 * Termux: API access android functions from Linux
 * Termux: Boot
 * Termux: Styling
 * Termux: Task (run Termux from tasker)
 
# set up ssh (port 8022 on termux)
 * https://glow.li/technology/2015/11/06/run-an-ssh-server-on-your-android-with-termux/
 * apt install openssh
 * sshd
 * touch ~/.ssh/authorized_keys
 * chmod 600 ~/.ssh/authorized_keys
 * chmod 700 ~/.ssh
 * ssh-keygen
 * cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
 * chmod 600 ~/.ssh/authorized_keys
 
# copy keys to sdcard (shows up under /phone instead /card)
 * cp ~/.ssh/id_rsa /sdcard
 
# convert id_rsa to id_rsa.ppk file if using putty
 * PuttyGen installed with putty on windows, use this to generate *.ppk

# ifconfig to find ip address of phone
 * run Putty, load key under connection-ssh-auth
 * I had to killall sshd on termux then restart sshd before it worked.

# termux-scripts
scripts for setting up termux for tinkering with neovim, python, tasker, etc.

setup_termux.sh - installs basic stuff for using python and neovim
 * curl -sSL https://raw.githubusercontent.com/chiplukes/termux-scripts/master/setup_termux.sh | bash

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
 


