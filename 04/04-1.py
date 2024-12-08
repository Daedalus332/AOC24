#variables
mapp = []
total = 0
utotal = 0
dtotal = 0
ltotal = 0
rtotal = 0
ultotal = 0
urtotal = 0
dltotal = 0
drtotal = 0

#initilisation, feeding file into mapp
with open("input.txt", "r") as f:
    linecount = 0
    for line in f:
        mapp.append([])
        for item in line:
            if item != "\n":
                mapp[linecount].append(item)
        linecount += 1


def find(mapp, placements):
    for line in mapp:
        if "X" in line:
            placementline = []
            placementlinenum = mapp.index(line)
            placementline = mapp[placementlinenum]
            placementchar = [i for i, e in enumerate(placementline) if e == "X"]
            for item in placementchar:
                placements.append([placementlinenum, item])

def checks(mapp, placements, line):
    doup = True
    dodown = True
    doleft = True
    doright = True
    lineplace = placements[0]
    charplace = placements[1]
    if lineplace - 4 < -1:
        doup = False
        
    if lineplace + 4 > len(mapp):
        dodown = False
        
    if charplace - 4 < -1:
        doleft = False

    if charplace + 4 > len(mapp[lineplace]):
        doright = False
    

    if doup == True:
        upcheck(mapp, lineplace, charplace)
        if doright == True:
            diaguprightcheck(mapp, lineplace, charplace)
        if doleft == True:
            diagupleftcheck(mapp, lineplace, charplace)
        
    if dodown == True:
        downcheck(mapp, lineplace, charplace)
        if doright == True:
            diagdownrightcheck(mapp, lineplace, charplace)
        if doleft == True:
            diagdownleftcheck(mapp, lineplace, charplace)

    if doleft == True:
        leftcheck(mapp, lineplace, charplace)
        
    if doright == True:
        rightcheck(mapp, lineplace, charplace)

def upcheck(mapp, lineplace, charplace):
    global utotal
    wordlist = []
    for x in range(0, 4):
        wordlist.append(mapp[lineplace - x][charplace])
    if "".join(wordlist) == "XMAS":
        utotal += 1
        
def downcheck(mapp, lineplace, charplace):
    global dtotal
    wordlist = []
    for x in range(0, 4):
        wordlist.append(mapp[lineplace + x][charplace])
    if "".join(wordlist) == "XMAS":
        dtotal += 1

def leftcheck(mapp, lineplace, charplace):
    global ltotal
    wordlist = []
    for x in range(0, 4):
        wordlist.append(mapp[lineplace][charplace - x])
    if "".join(wordlist) == "XMAS":
        ltotal += 1

def rightcheck(mapp, lineplace, charplace):
    global rtotal
    wordlist = []
    for x in range(0, 4):
        wordlist.append(mapp[lineplace][charplace + x])
    if "".join(wordlist) == "XMAS":
        rtotal += 1

def diaguprightcheck(mapp, lineplace, charplace):
    global urtotal
    wordlist = []
    for x in range(0, 4):
        wordlist.append(mapp[lineplace - x][charplace + x])
    if "".join(wordlist) == "XMAS":
        urtotal += 1

def diagupleftcheck(mapp, lineplace, charplace):
    global ultotal
    wordlist = []
    for x in range(0, 4):
        wordlist.append(mapp[lineplace - x][charplace - x])
    if "".join(wordlist) == "XMAS":
        ultotal += 1

def diagdownrightcheck(mapp, lineplace, charplace):
    global drtotal
    wordlist = []
    for x in range(0, 4):
        wordlist.append(mapp[lineplace + x][charplace + x])
    if "".join(wordlist) == "XMAS":
        drtotal += 1

def diagdownleftcheck(mapp, lineplace, charplace):
    global dltotal
    wordlist = []
    for x in range(0, 4):
        wordlist.append(mapp[lineplace + x][charplace - x])
    if "".join(wordlist) == "XMAS":
        dltotal += 1
    
placements = []
find(mapp, placements)
for x in range(0, len(placements)):
    checks(mapp, placements[x], item)
print(utotal, dtotal, ltotal, rtotal, ultotal, urtotal, dltotal, drtotal)
print(utotal + dtotal + ltotal + rtotal + ultotal + urtotal + dltotal + drtotal)
            
