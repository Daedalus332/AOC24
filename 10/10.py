mapp = []
coords = []
total = 0

with open("test.txt", "r") as f:
    linecount = 0
    for line in f:
        mapp.append([])
        for item in line:
            if item != "\n" and item != ".":
                mapp[linecount].append(int(item))
        linecount += 1
        

for x in range(0, len(mapp)):
    for y in range(0, len(mapp[x])):
        if mapp[x][y] == 0:
            coords.append([x, y])
print(coords)



def upcheck(placements):
    global coords
    global mapp
    global done
    if not done:
        if (mapp[placements[0]][placements[1]]) + 1 == (mapp[placements[0]-1][placements[1]]):
            coords.append([placements[0]-1, placements[1]])
            main([placements[0]-1, placements[1]])


def downcheck(placements):
    global coords
    global mapp
    global done
    if not done:
        if (mapp[placements[0]][placements[1]]) + 1 == (mapp[placements[0]+1][placements[1]]):
            coords.append([placements[0]+1, placements[1]])
            main([placements[0]+1, placements[1]])

def leftcheck(placements):
    global coords
    global mapp
    global done
    if not done:
        if (mapp[placements[0]][placements[1]]) + 1 == (mapp[placements[0]][placements[1]-1]):
            coords.append([placements[0], placements[1]-1])
            main([placements[0], placements[1]-1])

    
def rightcheck(placements):
    global coords
    global mapp
    global done
    if not done:
        if (mapp[placements[0]][placements[1]]) + 1 == (mapp[placements[0]][placements[1]+1]):
            coords.append([placements[0]-1, placements[1]+1])
            main([placements[0], placements[1]+1])




def main(item):
    global done
    global total
    if done == False:
        if item[0]-1 > 0:
            upcheck(item)

        if item[0] + 1 < len(mapp)-1:
            downcheck(item)

        if item[1] -1 != -1:
            leftcheck(item)

        if item[1]+1 < (len(mapp[1])-1):
            rightcheck(item)
        
        if (mapp[item[0]][item[1]] == 9):
            print("bing")
            total += 1
            done = True
        
        

for item in coords:
    done = False
    if item[0]-1 > 0:
        upcheck(item)
    done = False
    if item[0] + 1 < len(mapp)-1:
        downcheck(item)
    done = False
    if item[1] -1 != -1:
        leftcheck(item)
    done = False
    if item[1]+1 < (len(mapp[1])-1):
        rightcheck(item)
    print("bong")

print(total)