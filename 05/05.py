from collections import defaultdict
key = defaultdict(list)
fail = True
total = 0

with open("key.txt", "r") as f:
    for line in f:
        line = line[:-1]
        left = int(line.split("|")[0])
        right = int(line.split("|")[1])
        key[left].append(right)


with open("input.txt", "r") as f:
    for line in f:
        fail = True
        counter = 0
        linesplit = list(map(int, line.split(",")))
        for x in range(0, len(linesplit)):
            keyslist = list(key.keys())
            if (linesplit[x] in key.keys()):
                if (x+1 < len(linesplit)):
                    if linesplit[x+1] in key[linesplit[x]]:
                        counter += 1
        if counter == len(linesplit) -1:
            total += linesplit[len(linesplit)//2]
print(total)
