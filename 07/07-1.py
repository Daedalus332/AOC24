from collections import defaultdict
import itertools
supertotal = 0
supercounter = 0
lstleft = []
lstright = []
lst = ["+", "*", "|"]


#init, create a dict of all the numbers on the left and their corresponding right values
with open("input.txt", "r") as f:
    for line in f:
        line = line[:-1]
        lstleft.append(int(line.split(":")[0]))
        lstright.append(list(map(int, line.split(":")[1].split(" ")[1:len(line.split(":")[1].split(" "))])))


def mathematics(values):
    counter = 0
    while len(values) > 1:
        if counter % 2 == 0:
            if values[1] == "|":
                values.pop(1)
                values[0] = int(str(values[0]) + str(values[1]))
                values.pop(1)
                
            elif values[1] == "*":
                values[0] *= values[2]
                values.pop(1)
                values.pop(1)
                       
            elif values[1] == "+":
                values[0] += values[2]
                values.pop(1)
                values.pop(1)
        counter += 1

    total = values[0]
    return(total)



for x in range(0, len(lstleft)):
    totals = []
    values = list(lstright[x])
    possibilities = [p for p in itertools.product(lst, repeat=len(values)-1)]
    for z in range(0, len(possibilities)):
        values = list(lstright[x])
        counter = 1
        for item in possibilities[z]:
            values.insert(counter, item)
            counter += 2
        totals.append(mathematics(values))
        
    if lstleft[x] in totals:
        supertotal += lstleft[x]
    supercounter += 1
    if supercounter % 100 == 0:
        print("ping")

print(supertotal)

