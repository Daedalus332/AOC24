adjpass = True
incdecpass = True
safe = 0
count = 0

def adj(linelist):
    global adjpass
    linelist = list(map(int, linelist))
    for x in range(0, len(linelist)):
        if x+1 < len(linelist):
            if ((linelist[x] - linelist[x+1] > 3) or (linelist[x] - linelist[x+1] < -3)):
                adjpass = False
                
def incdec(linelist):
    global incdecpass
    asc = False
    desc = False
    linelist = list(map(int, linelist))
    for x in range(0, len(linelist)):
        if x+1 < len(linelist):
            if (linelist[x] - linelist[x+1] > 0):
                desc = True
            elif (linelist[x] - linelist[x+1] < 0):
                asc = True
            else:
                incdecpass = False
    if desc and asc:
        incdecpass = False

    
with open("input.txt", "r") as f:
    for line in f:
        var1 = False
        Count = -1
        Count2 = 0
        while var1 == False:
            Linesplit = line.split()
            if Count2 > 0:
                Linesplit.pop(Count )
            adjpass = True
            incdecpass = True
            adj(Linesplit)
            incdec(Linesplit)
            if ((adjpass and incdecpass)):
                var1 = True
                safe += 1
            elif (Count > len(Linesplit) - 1):
                var1 = True
            else:
                Count += 1
                Count2 += 1

print(safe)
