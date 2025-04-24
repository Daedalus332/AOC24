#variables
mapp = []
placements = []
supertotal = 0

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
    for line in range(1, len(mapp)-1):
        if "A" in mapp[line]:
            placementline = []
            placementlinenum = mapp.index(mapp[line])
            placementline = mapp[placementlinenum]
            placementchar = [i for i, e in enumerate(placementline) if e == "A"]
            for item in placementchar:
                if item > 0 and item < len(placementline)-1:
                    placements.append([placementlinenum, item])
                    
            
def checks(mapp, placements, line):
    global supertotal
    total = 0
    upright = False
    upleft = False
    downright = False
    downleft = False
    
    lineplace = placements[0]
    charplace = placements[1]

    wordlist1 = []
    for x in range(-1, 2):
        wordlist1.append(mapp[lineplace - x][charplace - x])
    if "".join(wordlist1) == "MAS":
        upleft = True
        
    wordlist2 = []
    for x in range(-1, 2):
        wordlist2.append(mapp[lineplace - x][charplace + x])
    if "".join(wordlist2) == "MAS":
        upright = True

    wordlist3 = []
    for x in range(-1, 2):
        wordlist3.append(mapp[lineplace + x][charplace - x])
    if "".join(wordlist3) == "MAS":
        downright = True

    wordlist4 = []
    for x in range(-1, 2):
        wordlist4.append(mapp[lineplace + x][charplace + x])
    if "".join(wordlist4) == "MAS":
        downleft = True

    if upright == True:
        total += 1
    if downright == True:
        total += 1
    if upleft == True:
        total += 1
    if downleft == True:
        total += 1

    if total == 2:
        supertotal += 1

find(mapp, placements)
for x in range(0, len(placements)):
    checks(mapp, placements[x], item)

print(supertotal)
