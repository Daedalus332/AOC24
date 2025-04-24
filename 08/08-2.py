from collections import defaultdict
coords = defaultdict(list)
linesplit = ""
counter = 0
linecounter = 0
mapp = []
mapp2 = []
total = 0

def subtractLists(l1, l2):
    return [l1[0] - l2[0], l1[1] - l2[1]]

def doubleList(l):
    return [l[0]*2, l[1]*2]

def addLists(l1, l2):
    return [l1[0] + l2[0], l1[1] + l2[1]]

def findDis(antennaType, antenna):
    for antennaCompare in coords[antennaType]:
        diff = subtractLists(antennaCompare, antenna)
        ogdiff = diff
        if diff != [0, 0]:
            for i in range(0, 100):
                diff = addLists(diff, ogdiff)
                antinodeCoords = addLists(antenna, diff)
                if antinodeCoords[1] < mapHeight and antinodeCoords[0] < mapWidth:
                    if antinodeCoords[1] >= 0 and antinodeCoords[0] >= 0:
                        mapp[antinodeCoords[1]] [antinodeCoords[0]] = "#"

with open("input.txt", "r") as f:
    for line in f:
        linesplit = list(line)
        mapp.append(linesplit)
        if '\n' in linesplit:
            linesplit.remove('\n')
        for item in linesplit:
            if item != ".":
                coords[item].append([counter%len(linesplit), linecounter])
            counter += 1
        linecounter += 1
    mapWidth = len(mapp[0])
    mapHeight = len(mapp)

    for antennaType in coords:
        for antenna in coords[antennaType]:
            
            findDis(antennaType, antenna)

for line in mapp:
    for item in line:
        if item != ".":
            total += 1

print(total)