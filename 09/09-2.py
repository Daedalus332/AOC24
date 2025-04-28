lis = []
counter = 0
length = 0
total = 0
last = 0
dotAmount = 0
dotFirst = 0
first = 0
start = 0
import time

dots = []

def find_last(lst, sought_elt):
    for r_idx, elt in enumerate(reversed(lst)):
        if elt == sought_elt:
            return len(lst) - 1 - r_idx

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
print(counter)
#print(lis)
for x in range(counter-1, -1, -1):
    #print(x)
    if x%100 == 0:
        print(x)
    dotAmount = 0 
   # tstart = time.time()
    for y in range(start, len(lis)):
        if lis[y] == ".":
            if dotAmount == 0:
                dotFirst = y
            dotAmount += 1
        else:
            if dotAmount > 0:
                if [dotFirst, dotAmount] not in dots:
                    dots.append([dotFirst, dotAmount])
                dotAmount = 0
    dots.sort(key=lambda x: x[0])
    #print("dots took", time.time()-tstart)
    #print(dots)

    length = 0

    #tstart = time.time()
    last = find_last(lis, x)
    #print("last took", time.time()-tstart)

   # tstart = time.time()
    for y in range(last, 0, -1):
        if lis[y] != x:
            first = y + 1
            break
        length += 1
    #print("first took", time.time()-tstart)

    #tstart = time.time()
    for item in dots:
        if item[1] >= length and item[0] < first:
            start = item[0]
            for y in range(0, length):
                lis[y + item[0]], lis[y + first] = lis[y + first], lis[y + item[0]]
            dots.remove(item)
            break
    #print("placement took", time.time()-tstart)
    #input()
    #print(lis)


#print(dots)
#print(first, last)
#print(length)
#print(lis)


#lis.pop(1)        
for x in range(0, len(lis)):
    if lis[x] != ".":
        total += lis[x] * x
print(total)
    