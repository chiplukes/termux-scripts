#!/data/data/com.termux/files/usr/bin/env python
import shlex
import subprocess
import sys

from darksky import forecast
from datetime import date, timedelta

def send_weather(wx_string):
    args = shlex.split("/data/data/com.termux/files/usr/bin/am broadcast "
                       "--user 0 "
                       "-a net.dinglish.tasker.wx "
                       "-e wxstring '{}' ".format(wx_string.replace("'","")
                                                ))
    subprocess.Popen(args)

if __name__ == "__main__":

    x = [a for a in sys.argv[1:]]
    api_key = "".join(x)

    BOZEMAN = 45.6770, 111.0429
    weekday = date.today()

    ret_str = "Good morning lazy folk, here is the weather forecast for Bozeman, MT."
    with forecast(api_key, *BOZEMAN) as bozeman:
        for day in bozeman.daily[:2]:
            day = dict(day = date.strftime(weekday, '%a'),
                    sum = day.summary,
                    tempMin = day.temperatureMin,
                    tempMax = day.temperatureMax
                    )
            ret_str += '{day}: {sum} Temp range: {tempMin} - {tempMax}'.format(**day)
            weekday += timedelta(days=1)
        ret_str += bozeman.daily.summary
    print(ret_str)

    #send_weather(sys.argv[1])
    send_weather(ret_str)
