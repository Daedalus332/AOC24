numlist = []
loopCount = 0
numAmounts = {}
total = 0

with open("test.txt", "r") as f:
    numList = list(map(int, f.read().split()))

for y in range(0, len(numlist)):
    print(numlist[x])
    item = numlist[x]
    for x in range(0, 5):
        if item == 0:
            numlist[x] = 1
        elif item % 2 == 0:
            half1 = int(item[0:n//2])
            half2 = int(item[n//2:])
            numlist.replace(x, half1)
            numlist.insert(x+1, half2)
        else:
            item *= 2024


print(numlist)


print(len(numList) + total)

