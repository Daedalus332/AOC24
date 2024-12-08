lis1 = []
lis2 = []
total = 0
with open ("input.txt", "r") as f:
    for line in f:
        lis = line.split()
        x = lis[0]
        y = lis[1]
        lis1.append(int(x))
        lis2.append(int(y))
for item in lis1:
    total += item * lis2.count(item)
print(total)
