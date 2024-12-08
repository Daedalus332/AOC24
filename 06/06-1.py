#variables
mapp = []
upbool = False
downbool = False
leftbool = False
rightbool = False
total = 0
counter = 0

#initilisation, feeding file into mapp

with open("input.txt", "r") as f:
    linecount = 0
    for line in f:
        mapp.append([])
        charcount = 0
        for item in line:
            if item != "\n":
                mapp[linecount].append(item)
        linecount += 1

#finding position of the guard in the map
def find(mapp):
    global upbool, downbool, leftbool, rightbool
    upbool = False
    downbool = False
    leftbool = False
    rightbool = False
    for line in mapp:
        if "^" in line:
            placementline = []
            placementlinenum = mapp.index(line)
            placementline = mapp[placementlinenum]
            placementchar = placementline.index("^")
            upbool = True
            return placementlinenum, placementchar
        elif ">" in line:
            placementline = []
            placementlinenum = mapp.index(line)
            placementline = mapp[placementlinenum]
            placementchar = placementline.index(">")
            rightbool = True
            return placementlinenum, placementchar
        elif "<" in line:
            placementline = []
            placementlinenum = mapp.index(line)
            placementline = mapp[placementlinenum]
            placementchar = placementline.index("<")
            leftbool = True
            return placementlinenum, placementchar
        elif "V" in line:
            placementline = []
            placementlinenum = mapp.index(line)
            placementline = mapp[placementlinenum]
            placementchar = placementline.index("V")
            downbool = True
            return placementlinenum, placementchar

def movement(placements):
    lineplace = placements[0]
    charplace = placements[1]
    global mapp
    global counter
    global upbool, downbool, leftbool, rightbool
    
    if lineplace - 1 == -1:
        upbool = False
        
    try:
        mapp[lineplace + 1]
    except IndexError:
        downbool = False
        
    if charplace - 1 == -1:
        leftbool = False
        
    try:
        mapp[charplace + 1]
    except IndexError:
        rightbool == False

        
    if upbool == True:
        if mapp[lineplace - 1][charplace] != "#":
            mapp[lineplace - 1][charplace] = "^"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = ">"
    elif downbool == True:
        if mapp[lineplace + 1][charplace] != "#":
            mapp[lineplace + 1][charplace] = "V"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = "<"
    elif leftbool == True:
        if mapp[lineplace][charplace - 1] != "#":
            mapp[lineplace][charplace - 1] = "<"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = "^"
    elif rightbool == True:
        if mapp[lineplace][charplace + 1] != "#":
            mapp[lineplace][charplace + 1] = ">"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = "V"
            
        


#main code
#for item in mapp:
#    print(item)
#print("breaker")
x = 0
while True:
    placements = find(mapp)
    movement(placements)
    #for item in mapp:
        #print(item)
    if counter % 10000 == 0:
        print("bing")
    if (not upbool) and (not downbool) and (not leftbool) and (not rightbool):
        break
    
for line in mapp:
    for item in line:
        if item == "B" or item == "V" or item == ">" or item == "<" or item == "^":
            total += 1
with open("other.txt", "w") as f:
    for line in mapp:
        f.write(str(line))
        f.write("\n")


print(total)

