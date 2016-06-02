import plotme
from callmap import callmap
from naviestbl import naviestable

import re


clsanalyse = naviestable()
clsanalyse.setpackageCount(3)
clsanalyse.setNumberOfPeriods(2)
clsanalyse.drawhistograms()
clsanalyse.set_judge_limits(10)
clsanalyse.takejudgement()
clsanalyse.getprobability(2, 1)





calldue = plotme.callduration()
calldate = plotme.calldate()

callduesec = []
calltimeinsec = []

timer = []

for call in calldue:
    h, m, s = call.split(":")
    callsec = h*3600 + m*60 + s
    callduesec.append(int(callsec))

"""
for time in calldate:
    calltime = time[11:19]
    print calltime
    h = calltime[0:2]
    print h
    m = calltime[3:5]
    print m
    s = calltime[6:8]
    print s
    timesec = int(h)*3600+int(m)*60+int(s)
    print timesec
    timer.append(timesec)

"""

map = callmap()
map.plot_hist(callduesec)

mapbar = callmap()
mapbar.plot_bar(callduesec)







