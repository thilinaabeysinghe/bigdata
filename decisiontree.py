from callduration import getcallduration
from callcount import getcallcount


durationlist = getcallduration()
callcountlist = getcallcount()


maxprobability = 0
minprobability = 1
tmppro = []

period = 0
counter = 0
for duration in durationlist:
    period = period + 1
    for count in callcountlist:
        counter = counter + 1
        probability = duration * count
        if probability > maxprobability:
            maxprobability = probability
        tmppro.append("period"+str(period)+" and count "+str(counter)+" get probability of #"+str(probability))
    counter = 0

print maxprobability

for sortitem in  tmppro:
    print sortitem


def triangleArea(x,y):
    return 0.5 * x * y

area = []
dummyarea = []

def ajusttotargetrevenue(duration, unitprice):
    for x in duration:
        area.append(triangleArea(x,unitprice))


def dummyajusttotargetrevenue(duration, unitprice):
    for x in duration:
        for y in unitprice:
            dummyarea.append(triangleArea(x,y))


bestpackages = []

def compair(area, dummy):
    for actualarea in area:
        for dummyarea in dummy:
            if actualarea < dummyarea:
                bestpackages.append(dummyarea*2)
    bestpackages.sort(reverse=True)
    for pack in bestpackages:
        print pack

def decision(current_unitprice, maximumrevenue):
    ajusttotargetrevenue(durationlist,current_unitprice)
    dummyajusttotargetrevenue(durationlist,range(current_unitprice,maximumrevenue,1))
    compair(area,dummyarea)

decision(2,5)
