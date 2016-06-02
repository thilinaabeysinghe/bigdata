from callduration import getcallduration
from callcount import getcallcount


durationlist = getcallduration()
callcountlist = getcallcount()


maxprobability = 0
minprobability = 1

for duration in durationlist:
    for count in callcountlist:
        probability = duration * count
        if probability > maxprobability:
            maxprobability = probability

print maxprobability