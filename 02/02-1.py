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

def checker(linelist):
    global adjpass
    global incdecpass
    global safe
    adjpass = True
    incdecpass = True
    adj(linelist)
    incdec(linelist)
    if incdecpass and adjpass:
        return True
    else:
        return False
    
with open("test.txt", "r") as f:
    for line in f:
        linelist = line.split()
        if checker(linelist) == True:
            safe += 1

            
            
        
                    

print(safe)
