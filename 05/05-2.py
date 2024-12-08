from collections import defaultdict
import itertools
import random
import sys
sys.setrecursionlimit(100000000)
key = defaultdict(list)
otherdict = {}
sorte = False
total = 0
total1 = 0
nums = []
    
with open("key.txt", "r") as f:
    for line in f:
        line = line[:-1]
        left = int(line.split("|")[0])
        right = int(line.split("|")[1])
        key[left].append(right)
        

def checker(linesplit):
    global counter
    global total
    counter = 0
    for x in range(0, len(linesplit)):
        keyslist = list(key.keys())
        if (linesplit[x] in key.keys()):
            if (x+1 < len(linesplit)):
                if linesplit[x+1] in key[linesplit[x]]:
                    counter += 1
    if counter == len(linesplit) - 1:
        total += linesplit[len(linesplit)//2]
    else:
        sorter(linesplit)

def checker2(linesplit):
    global counter
    global total1
    global sorte
    counter = 0
    for x in range(0, len(linesplit)):
        keyslist = list(key.keys())
        if (linesplit[x] in key.keys()):
            if (x+1 < len(linesplit)):
                if linesplit[x+1] in key[linesplit[x]]:
                    counter += 1
    if counter == len(linesplit) - 1:
        total1 += linesplit[len(linesplit)//2]
        sorte = True
        print(total1)


def sorter(linesplit):
    global sorte
    returner = list((itertools.permutations(linesplit, len(linesplit))))
    for x in range(0, len(returner)):
        if sorte == True:
            break
        checker2(returner[x])
    
        
with open("input.txt", "r") as f:
    for line in f:
        counter = 0
        sorte = False
        linesplit = list(map(int, line.split(",")))
        checker(linesplit)
print(total1)
