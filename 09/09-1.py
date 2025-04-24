lis = []
counter = 0
total = 0

with open("input.txt", "r") as f:
    for item in f:
        item = list(map(int, item))
        for x in range(0, len (item)):
            for y in range(0, item[x]):
                if x % 2 == 0:
                    lis.append(counter)
                else:
                    lis.append(".")
            if x % 2 == 0:
                counter += 1
print("beep")

for x in range(len(lis)-1, 0, -1):
    if "." in lis:
        dotplace = lis.index(".")
    if lis[x] != ".":
        lis[dotplace] = lis[x]
        lis[x] = "."

    if x % 1000 == 0:
        print(x)

lis.pop(1)        
for x in range(0, len(lis)):
    if lis[x] == ".":
        break
    total += lis[x] * x
print(total)
    