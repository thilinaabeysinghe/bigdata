from datagrabber import openfile
from numpy import *
import matplotlib.pyplot as plt

class naviestable():
    #packges
    packages = []
    #duration periods
    periods = 2

    #store number of periods
    numperiods = 0

    #store data list
    datastore = []

    #store output count order by periods divide
    periodcountvalues = []

    #judgement line
    judgeline = 1

    #judgement list
    judge = []

    #set package count
    def setpackageCount(self, pkg):
        self.packages = pkg

    def setNumberOfPeriods(self, numperiod):
        self.numperiods = numperiod

    #set call durations sets parse a list
    def  setcalldurations(self, period):
        self.periods = period

    #get data from input file
    def getdata(self):
        data = openfile()
        for row in data:
            self.datastore.append(str(row[17]))

    #draw histograms for time periods
    def drawhistograms(self):


        #get size of a period
        #periodsize = len(self.periods)

        #if periodsize > self.numperiods:
        periodcount = 1
        start = 0
        for period in range(self.periods):
            end = self.periods / self.numperiods * period
            counts, bins, bars = plt.hist(self.datastore[start:end], histtype="bar", label="Peak", color="red", stacked=True)
            self.periodcountvalues.append(counts)
            start = end

    #judge limit of calls duration above
    def set_judge_limits(self, limit):
        self.judgeline = limit

    #take judgement
    def takejudgement(self):

        for c in self.periodcountvalues:
            if self.judgeline < c:
                self.judge.append(True)
            else:
                self.judge.append(False)

    #get number of periods for a perticular package
    def getnumYesPeriodsInpackage(self, packageid, periodid):
        numYes = 0
        countval = 1
        for val in self.judge:
            if countval / periodid == packageid and val == True:
                numYes = numYes + 1
                countval = countval + 1
        return numYes

    #get number of periods for a perticular package
    def getnumNoPeriodsInpackage(self, packageid, periodid):
        numNo = 0
        countval = 1
        for val in self.judge:
            if countval / periodid == packageid and val == False:
                numNo = numNo + 1
                countval = countval + 1
        return numNo




    #get probability of call taken by package number and time frame
    def getprobability(self,packageid, periodid):
        yes = self.getnumYesPeriodsInpackage(packageid,periodid)
        no = self.getnumNoPeriodsInpackage(packageid,periodid)

        print yes / (yes+no)







