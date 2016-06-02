#import numpy as np
import csv
import string
calltime = []
returncount = []


def getcallcount():
    with open('cdr.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter='|')
        for unitcall in plots:
            calltime.append(str(unitcall[14]))


    period1 = 0
    period2 = 0
    period3 = 0
    period4 = 0
    period5 = 0
    period6 = 0

    for timein in calltime:
        print timein
        h = timein[11:13]
        print h

        parseStr = lambda x: x.isalpha() and x or x.isdigit() and int(x) or x.isalnum() and x or len(set(string.punctuation).intersection(x)) == 1 and x.count('.') == 1 and float(x) or x

        hour = parseStr(h)

        if hour >= 0 and hour < 4:
            period1 = period1 + 1
        elif hour >= 4 and hour < 8:
            period2 = period2 + 1
        elif hour >= 8 and hour < 12:
            period3 = period3 + 1

        elif hour >= 12 and hour < 16:
            period4 = period4 + 1

        elif hour >= 16 and hour < 20:
            period5 = period5 + 1

        elif hour >= 20 and hour < 24:
            period6 = period6 + 1
        else:
            print "0000000"

    total = period1 + period2 + period3 + period4 + period5 + period6

    print total

    print "Period 1 " + str(period1)+ "percentage : "+str(float(period1) / float(total))
    print "Period 2 " + str(period2)+ "percentage : "+str(float(period2 / float(total)))
    print "Period 3 " + str(period3)+ "percentage : "+str(float(period3 / float(total)))
    print "Period 4 " + str(period4)+ "percentage : "+str(float(period4 / float(total)))
    print "Period 5 " + str(period5)+ "percentage : "+str(float(period5 / float(total)))
    print "Period 6 " + str(period6)+ "percentage : "+str(float(period6 / float(total)))


    callcountavgl = []
    callcountavgl.append(float(period1) / float(float(period1) / float(total)))
    callcountavgl.append(float(period2) / float(float(period2) / float(total)))
    callcountavgl.append(float(period3) / float(float(period3) / float(total)))
    callcountavgl.append(float(period4) / float(float(period4) / float(total)))
    callcountavgl.append(float(period5) / float(float(period5) / float(total)))
    callcountavgl.append(float(period6) / float(float(period6) / float(total)))

    return callcountavgl




