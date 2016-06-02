from numpy import *
import matplotlib.pyplot as plt



class callmap():
    def plot_hist(self, a):

        size = len(a)
        timeperiod1 = (size/2)*1
        counts, bins, bars = plt.hist(a[0:timeperiod1], histtype="bar", label="Peak", color="red", stacked=True)
        counts2, bins2, bars2 = plt.hist(a[timeperiod1:size], histtype="bar", label="Off-Peak", color="blue" , stacked=True)
        plt.show()

    def plot_bar(self, a):
        size = len(a)
        timeperiod1 = (size / 24) * 1
        timeperiod2 = (size / 24) * 2
        timeperiod3 = (size / 24) * 3
        timeperiod4 = (size / 24) * 4
        timeperiod5 = (size / 24) * 5
        timeperiod6 = (size / 24) * 6
        timeperiod7 = (size / 24) * 7
        timeperiod8 = (size / 24) * 8
        timeperiod9 = (size / 24) * 9
        timeperiod10 = (size / 24) * 10
        timeperiod11 = (size / 24) * 11
        timeperiod12 = (size / 24) * 12
        timeperiod13 = (size / 24) * 13
        timeperiod14 = (size / 24) * 14
        timeperiod15 = (size / 24) * 15
        timeperiod16 = (size / 24) * 16
        timeperiod17 = (size / 24) * 17
        timeperiod18 = (size / 24) * 18
        timeperiod19 = (size / 24) * 19
        timeperiod20 = (size / 24) * 20
        timeperiod21 = (size / 24) * 21
        timeperiod22 = (size / 24) * 22
        timeperiod23 = (size / 24) * 23
        timeperiod24 = (size / 24) * 24


        counts1, bins1, bars1 = plt.hist(a[0:timeperiod1], label="Peak", color="red" , alpha=0.7)
        counts2, bins2, bars2 = plt.hist(a[timeperiod1:timeperiod2], label="Off-Peak", color="red", alpha=0.7)
        counts3, bins3, bars3 = plt.hist(a[timeperiod2:timeperiod3], label="Off-Peak", color="red", alpha=0.7)
        counts4, bins4, bars4 = plt.hist(a[timeperiod3:timeperiod4], label="Off-Peak", color="red", alpha=0.7)
        counts5, bins5, bars5 = plt.hist(a[timeperiod4:timeperiod5], label="Off-Peak", color="red", alpha=0.7)
        counts6, bins6, bars6 = plt.hist(a[timeperiod5:timeperiod6], label="Peak", color="red", alpha=0.7)
        counts7, bins7, bars7 = plt.hist(a[timeperiod6:timeperiod7], label="Off-Peak", color="red", alpha=0.7)
        counts8, bins8, bars8 = plt.hist(a[timeperiod7:timeperiod8], label="Off-Peak", color="red", alpha=0.7)
        counts9, bins9, bars9 = plt.hist(a[timeperiod8:timeperiod9], label="Off-Peak", color="red", alpha=0.7)
        counts10, bins10, bars10 = plt.hist(a[timeperiod9:timeperiod10], label="Off-Peak", color="red", alpha=0.7)
        counts11, bins11, bars11 = plt.hist(a[timeperiod10:timeperiod11], label="Peak", color="red", alpha=0.7)
        counts12, bins12, bars12 = plt.hist(a[timeperiod11:timeperiod12], label="Off-Peak", color="red", alpha=0.7)
        counts13, bins13, bars13 = plt.hist(a[timeperiod12:timeperiod13], label="Off-Peak", color="green", alpha=0.7)
        counts14, bins14, bars14 = plt.hist(a[timeperiod13:timeperiod14], label="Off-Peak", color="green", alpha=0.7)
        counts15, bins15, bars15 = plt.hist(a[timeperiod14:timeperiod15], label="Off-Peak", color="green", alpha=0.7)
        counts16, bins16, bars16 = plt.hist(a[timeperiod15:timeperiod16], label="Peak", color="green", alpha=0.7)
        counts17, bins17, bars17 = plt.hist(a[timeperiod16:timeperiod17], label="Off-Peak", color="green", alpha=0.7)
        counts18, bins18, bars18 = plt.hist(a[timeperiod17:timeperiod18], label="Off-Peak", color="green", alpha=0.7)
        counts19, bins19, bars19 = plt.hist(a[timeperiod18:timeperiod19], label="Off-Peak", color="green", alpha=0.7)
        counts20, bins20, bars20 = plt.hist(a[timeperiod19:timeperiod20], label="Off-Peak", color="green", alpha=0.7)
        counts21, bins21, bars21 = plt.hist(a[timeperiod20:timeperiod21], label="Off-Peak", color="green", alpha=0.7)
        counts22, bins22, bars22 = plt.hist(a[timeperiod21:timeperiod22], label="Peak", color="green", alpha=0.7)
        counts23, bins23, bars23 = plt.hist(a[timeperiod22:timeperiod23], label="Off-Peak", color="green", alpha=0.7)
        counts24, bins24, bars24 = plt.hist(a[timeperiod23:timeperiod24], label="Off-Peak", color="green", alpha=0.7)

        print counts1

        session1 = []
        session2 = []
        session3 = []
        session4 = []
        session5 = []

        session1.append(counts1)
        session1.append(counts2)
        session1.append(counts3)
        session1.append(counts4)
        session1.append(counts5)

        session2.append(counts6)
        session2.append(counts7)
        session2.append(counts8)
        session2.append(counts9)
        session2.append(counts10)

        session3.append(counts11)
        session3.append(counts12)
        session3.append(counts13)
        session3.append(counts14)
        session3.append(counts15)

        session4.append(counts16)
        session4.append(counts17)
        session4.append(counts18)
        session4.append(counts19)
        session4.append(counts20)

        session5.append(counts21)
        session5.append(counts22)
        session5.append(counts23)
        session5.append(counts24)


        print "Report of the Result"
        print "00.00 - 05.00"
        print sum(session1)

        print "Report of the Result"
        print "05.00 - 10.00"
        print sum(session2)

        print "Report of the Result"
        print "10.00 - 15.00"
        print sum(session3)

        print "Report of the Result"
        print "15.00 - 20.00"
        print sum(session4)

        print "Report of the Result"
        print "20.00 - 24.00"
        print sum(session5)


        plt.show()

    def plot_dueandtime(self, a, b):
        size = len(a)
        timeperiod1 = (size / 2) * 1
        x1 = range(0, timeperiod1, 1)
        x2 = range(timeperiod1, size, 1)
        plt.plot(a[0:timeperiod1], b[0:timeperiod1], label="Peak", color="green")
        plt.plot(a[timeperiod1:size], b[timeperiod1:size], label="Peak", color="blue")

        plt.show()










