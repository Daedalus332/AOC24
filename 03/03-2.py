import re
import math
total = 0
with open("input.txt", "r")as f:
    lis = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", f.read())
    for item in lis:
        item = item[4:]
        item = item[:-1]
        testlist = item.split(",")
        testlist = list(map(int, testlist))
        total += math.prod(testlist)
print(total)
