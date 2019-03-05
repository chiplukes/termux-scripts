#!/data/data/com.termux/files/usr/bin/env python
import shlex
import subprocess
import sys

def send_weather(wx_string):
    args = shlex.split("/data/data/com.termux/files/usr/bin/am broadcast "
                       "--user 0 "
                       "-a net.dinglish.tasker.wx "
                       "-e wxstring '{}' ".format(wx_string.replace("'","")
                                                ))
    subprocess.Popen(args)

if __name__ == "__main__":

    
    #send_weather(sys.argv[1])
    x = [a for a in sys.argv[1:]]
    msg = "".join(x)
    send_weather(msg)
