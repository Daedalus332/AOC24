lis1 = []
lis2 = []
with open ("input.txt", "r") as f:
    for line in f:
        lis = line.split()
        x = lis[0]
        y = lis[1]
        lis1.append(int(x))
        lis2.append(int(y))
lis1.sort()
lis2.sort()
total = 0
totaltotal = 0
totaltotal = 0
for i in range(0, len(lis1)):
  total = lis1[i] - lis2[i]
  if total < 0:
    total *= -1
  totaltotal += total
print(totaltotal)
