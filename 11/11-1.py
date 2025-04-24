numlist = []

with open("input.txt", "r") as f:
    numlist = list(map(int, f.read().split()))

for z in range(0, 25):
    #print("blink")
    y=1
    x = 0
    while x < len(numlist):
        item = str(numlist[x])
        n = len(item)
        if n % 2 == 0:
            string1 = item[0:n//2]
            string2 = item[n//2:]
            numlist.insert(x+1, int(string2))
            numlist[x] = (int(string1))
            x += 2
        elif item == "0":
            numlist[x] = 1
            x += 1
        else:
            numlist[x] *= 2024
            x += 1

print(len(numlist))

