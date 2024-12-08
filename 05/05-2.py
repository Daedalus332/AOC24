from collections import defaultdict
import random
key = defaultdict(list)
otherdict = {}
fail = True
total = 0
nums = []
    
with open("testkey.txt", "r") as f:
    for line in f:
        line = line[:-1]
        left = int(line.split("|")[0])
        right = int(line.split("|")[1])
        key[left].append(right)

with open("testkey.txt", "r") as f:
    doc = f.read()
    doc = doc.replace("|", " ")
    doc = doc.replace("\n", " ")
    doc = list(map(int, doc.split()))
    for x in range(0, len(doc)):
        if doc[x] in key.keys():
            keyslist = list(key.keys())
            l = keyslist.index(doc[x])
            keyvalues = list(key.values())
            otherdict[doc[x]] = len(keyvalues[l])
        else:
            otherdict[doc[x]] = 0

def checker(linesplit):
    global counter
    global fail
    global total
    for x in range(0, len(linesplit)):
        keyslist = list(key.keys())
        if (linesplit[x] in key.keys()):
            if (x+1 < len(linesplit)):
                if linesplit[x+1] in key[linesplit[x]]:
                    counter += 1
    if counter == len(linesplit) - 1:
        total += linesplit[len(linesplit)//2]
    else:
        print(linesplit)
        linesplit = sorter(linesplit)
        print(linesplit)
        checker(linesplit)

def sorter(linesplit):
    templist = []
    for item in linesplit:
        templist.append(otherdict[item])
    templist, linesplit = (list(t) for t in zip(*sorted(zip(templist,linesplit))))
    return linesplit
                    
with open("testinput.txt", "r") as f:
    for line in f:
        fail = True
        counter = 0
        linesplit = list(map(int, line.split(",")))
        checker(linesplit)
print(total)
