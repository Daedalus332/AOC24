#variables
mapp = []
mappp = []
blockerlist = []
trackerlist = []
supertotal = 0
loop = False
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
    global loop
    global mapp
    global trackerlist
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
        if ([lineplace - 1, charplace, "^"]) in trackerlist:
            #print(mapp)
            #print([lineplace - 1, charplace, "^"])
            loop = True
            
        if mapp[lineplace - 1][charplace] != "#":
            mapp[lineplace - 1][charplace] = "^"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = ">"
            trackerlist.append([lineplace -1, charplace, "^"])
            
            
    elif downbool == True:
        if ([lineplace + 1, charplace, "V"]) in trackerlist:
            #print([lineplace + 1, charplace, "V"])
            loop = True
            
        if mapp[lineplace + 1][charplace] != "#":
            mapp[lineplace + 1][charplace] = "V"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = "<"
            trackerlist.append([lineplace + 1, charplace, "V"])
            
            
    elif leftbool == True:
        if ([lineplace, charplace - 1, "<"]) in trackerlist:
            #print([lineplace, charplace - 1, "<"])
            loop = True
            
        if mapp[lineplace][charplace - 1] != "#":
            mapp[lineplace][charplace - 1] = "<"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = "^"
            trackerlist.append([lineplace, charplace - 1, "<"])
            

    elif rightbool == True:
        if ([lineplace, charplace + 1, ">"]) in trackerlist:
            #print([lineplace, charplace + 1, ">"])
            loop = True
        if mapp[lineplace][charplace + 1] != "#":
            mapp[lineplace][charplace + 1] = ">"
            mapp[lineplace][charplace] = "B"
            counter += 1
        else:
            mapp[lineplace][charplace] = "V"
            trackerlist.append([lineplace, charplace + 1, ">"])
            
            
        


#main code            
def main():
    global supertotal
    global loop
    while True:
        placements = find(mapp)
        movement(placements)
        if (not upbool) and (not downbool) and (not leftbool) and (not rightbool):
            break
        if loop == True:
            supertotal += 1
            break
mapp = []    
init()
ogplacement = find(mapp)
print(ogplacement)
main()
mappp = list(mapp)
mapp = []
init()
        
for line in range(0, len(mappp)):
    for item in range(0, len(mappp[line])):
        if (mappp[line][item] == "B" or mappp[line][item] == "^" or mappp[line][item] == "V") and ((line, item) != ogplacement):
            trackerlist = []
            loop = False
            mapp[line][item] = "#"
            
            #print(line, item)
            #for item in mapp:
            #    print(item)
            #print("br")
            main()
            mapp = []
            init()
            print(supertotal)
            
print(supertotal)          
#init()
#print(len(blockerlist))
#for x in range(0, len(blockerlist)):
#    mapp[blockerlist[x][0]][blockerlist[x][1]] = "#"
#    main()


