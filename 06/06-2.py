#variables
mapp = []
mappp = []
blockerlist = []
upbool = False
downbool = False
leftbool = False
rightbool = False
total = 0
counter = 0

#initilisation, feeding file into mapp
def init():
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
        rightbool = False

        
    if upbool == True:
        if mapp[lineplace - 1][charplace] != "#" or "1" or "2":
            mapp[lineplace - 1][charplace] = "^"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = ">"
            if mapp[lineplace - 1][charplace] == "1":
                mapp[lineplace - 1][charplace] = "2"
            else:
                mapp[lineplace - 1][charplace] = "1"
    elif downbool == True:
        if mapp[lineplace + 1][charplace] != "#" or "1":
            mapp[lineplace + 1][charplace] = "V"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = "<"
            if mapp[lineplace + 1][charplace] == "1":
                mapp[lineplace + 1][charplace] = "2"
            else:
                mapp[lineplace + 1][charplace] = "1"
    elif leftbool == True:
        if mapp[lineplace][charplace - 1] != "#" or "1":
            mapp[lineplace][charplace - 1] = "<"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = "^"
            if mapp[lineplace][charplace - 1] == "1":
                mapp[lineplace][charplace - 1] = "2"
            else:
                mapp[lineplace][charplace - 1] = "1"
    elif rightbool == True:
        if mapp[lineplace][charplace + 1] != "#" or "1":
            mapp[lineplace][charplace + 1] = ">"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = "V"
            if mapp[lineplace][charplace + 1] == "1":
                mapp[lineplace][charplace + 1] = "2"
            else:
                mapp[lineplace][charplace + 1] = "1"
            
        


#main code            
def main():
    while True:
        placements = find(mapp)
        movement(placements)
        if (not upbool) and (not downbool) and (not leftbool) and (not rightbool):
            break
    
        
init()
main()
with open("other-other.txt", "w") as f:
    for line in mapp:
        f.write((str(line)))
        f.write("\n")
for line in mapp:
    if "B" in line:
        placementline = []
        placementlinenum = mapp.index(line)
        placementline = mapp[placementlinenum]
        placementchar = placementline.index("B")
        placements = (placementlinenum, placementchar)
        blockerlist.append(placements)
init()
for x in range(0, len(blockerlist)):
    mapp[blockerlist[0]][blockerlist[1]] = "#"
    main()


