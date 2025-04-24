from collections import defaultdict
key = defaultdict(list)
fail = True
total = 0
total2 = 0

def checker(line):
    global total
    fail = True
    counter = 0
    linesplit = list(map(int, line.split(",")))
    for x in range(0, len(linesplit)):
        if (linesplit[x] in key.keys()):
            if (x+1 < len(linesplit)):
                if linesplit[x+1] in key[linesplit[x]]:
                    counter += 1
    if counter == len(linesplit) -1:
        total += linesplit[len(linesplit)//2]
    else:
        sorter(linesplit)

def checker2(linesplit):
    global total2
    fail = True
    counter = 0
    for x in range(0, len(linesplit)):
        if (linesplit[x] in key.keys()):
            if (x+1 < len(linesplit)):
                if linesplit[x+1] in key[linesplit[x]]:
                    counter += 1
    if counter == len(linesplit) -1:
        total2 += linesplit[len(linesplit)//2]
    else:
        sorter(linesplit)

def sorter(line):
    print(line)
    for x in range(0, len(line)-1):
        if line[x] in key.keys():
            if (line[x+1] not in key[line[x]]):
                line[x], line[x+1] = line[x+1], line[x]
        else:
            line[x], line[-1] = line[-1], line[x]
    checker2(line)


with open("key.txt", "r") as f:
    for line in f:
        line = line[:-1]
        left = int(line.split("|")[0])
        right = int(line.split("|")[1])
        key[left].append(right)


with open("input.txt", "r") as f:
    for line in f:
        checker(line)




print(total2)
