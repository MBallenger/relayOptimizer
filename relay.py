import itertools
from itertools import combinations
from itertools import groupby
import operator
from operator import itemgetter


class Swimmer:

    def __init__(self, name, age, sex, time50Free):
        self.name = name
        self.age = age
        self.sex = sex
        self.time50Free = time50Free

    def createWSwimmerList():
        womensSwimmerList = [
            Swimmer("Marie Ballenger", 37, "F", 24.00),
            Swimmer("Laureen Welting", 50, "F", 27.00),
            Swimmer("Courtney Monsees", 35, "F", 24.00),
            Swimmer("Felica Lee", 30, "F", 23.00),
            Swimmer("Dierdre Clute", 28, "F", 24.00),
            Swimmer("Cat Ladd", 27, "F", 24.50),
            Swimmer("Naoko Watanabe", 40, "F", 25.00),
            Swimmer("Allison Arnold", 32, "F", 25.00),
            Swimmer("Kendyl Stewart", 24, "F", 23.00),
            Swimmer("Erica Schreer", 36, "F", 25.00),
            Swimmer("Lauren Green", 23, "F", 23.00),
        ]
        return womensSwimmerList


def createRelayCombinations():
    swimList = Swimmer.createWSwimmerList()
    relays = list(itertools.combinations(swimList, 4))
    global relaysDictList
    relaysDictList = []
    for i in range(len(relays)):
        print(i, end=" ")
        relay = relays[i]
        minAge = relay[0].age
        estRelayTime = 0
        ageGroup = 0
        relayDict = {}
        for j in range(len(relay)):
            relaySwimmer = relay[j]
            relayDict["swimmer" + str(j+1)] = relaySwimmer.name
            relayDict["swimmer" + str(j+1) + "Time"] = relaySwimmer.time50Free
            estRelayTime += relaySwimmer.time50Free
            if relaySwimmer.age < minAge:
                minAge = relaySwimmer.age
        if minAge < 25:
            ageGroup = 18
        else:
            ageGroup = 5 * round(minAge/5)
        relayDict["ageGroup"] = ageGroup
        relayDict["relayTime"] = estRelayTime
        relaysDictList.append(relayDict)
    return relaysDictList

def sortRelays():   
    createRelayCombinations()
    # Sort relays by ageGroup.
    relaysDictListSorted = sorted(relaysDictList, key = itemgetter("ageGroup"))
 
    # Display data grouped by ageGroup
    sortedRelays = {}
    for key, value in groupby(relaysDictListSorted, key = itemgetter("ageGroup")):
        print("\n")
        sortedRelays['%s' % key] = []
        for k in value:
            sortedRelays['%s' % key].append(k)
        sortedRelays['%s' % key] = sorted(sortedRelays['%s' % key], key = itemgetter("relayTime"))

sortRelays()