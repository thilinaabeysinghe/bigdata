#import numpy as np
import csv
import string
calltime = []
callduration = []
returnduration = []


def getcallduration():
    with open('cdr.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter='|')
        for unitcall in plots:
            calltime.append(str(unitcall[14]))
            callduration.append(str(unitcall[17]))

    period1totalcall = 0
    period2totalcall = 0
    period3totalcall = 0
    period4totalcall = 0
    period5totalcall = 0

    for index in range(len(calltime)):
        timein = calltime[index]
        timedura = callduration[index]
        htime = timein[11:13]

        h = timedura[0:2]
        m = timedura[3:5]
        s = timedura[6:8]

        print timedura
        print "%s %s %s" % (h, m, s)


        parseStr = lambda x: x.isalpha() and x or x.isdigit() and int(x) or x.isalnum() and x or len(set(string.punctuation).intersection(x)) == 1 and x.count('.') == 1 and float(x) or x

        hour = parseStr(htime)

        hourd = parseStr(h)
        min = parseStr(m)
        sec = parseStr(s)

        total_time = int(hourd) * 3600 + int(min) * 60 + int(sec)

        rangecall = int(min) * 60 + int(sec)

        if rangecall >= 0 and rangecall < 30:
            period1totalcall += total_time
        elif rangecall >= 30 and rangecall < 120:
            period2totalcall += total_time
        elif rangecall >= 120 and rangecall < 300:
            period3totalcall += total_time
        elif rangecall >= 300 and rangecall < 600:
            period4totalcall += total_time
        else:
            period5totalcall += total_time

    totaltime = period1totalcall + period2totalcall + period3totalcall + period4totalcall + period5totalcall



    print "Period 1 " + str(period1totalcall)+ "percentage : "+str(float(period1totalcall) / float(totaltime))
    print "Period 2 " + str(period2totalcall)+ "percentage : "+str(float(period2totalcall) / float(totaltime))
    print "Period 3 " + str(period3totalcall)+ "percentage : "+str(float(period3totalcall) / float(totaltime))
    print "Period 4 " + str(period4totalcall)+ "percentage : "+str(float(period4totalcall) / float(totaltime))
    print "Period 5 " + str(period5totalcall)+ "percentage : "+str(float(period5totalcall) / float(totaltime))


    durationavg = []
    durationavg.append(float(period1totalcall) / float(totaltime))
    durationavg.append(float(period2totalcall) / float(totaltime))
    durationavg.append(float(period3totalcall) / float(totaltime))
    durationavg.append(float(period4totalcall) / float(totaltime))
    durationavg.append(float(period5totalcall) / float(totaltime))

    return  durationavg



