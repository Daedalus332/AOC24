trailheadcoords = []
mapp = []
xcount = 0
ycount = 0

def scanSurroundings(coords):
	current = mapp[coords[0]][coords[1]]
	if current == 9:
		total += 1
		return
	else:
		target = current + 1
		if coords[0] - 1 >= 0:
			if target == mapp[coords[0]-1][coords[1]]:
				scanSurroundings[]
		if coords[1] - 1 >= 0:
		if coords[0] + 1 <= xcount:
		if coords[1] -1 <= ycount:

with open("test.txt", "r") as f:
	for line in f:
		linesplit = list(line)
		if '\n' in linesplit:
			linesplit.remove('\n')
		mapp.append(linesplit)

for line in mapp:
	xcount = 0
	for item in line:
		if item == "0":
			trailheadcoords.append([xcount, ycount])
		xcount += 1
	ycount += 1

for trailhead in trailheadcoords:
	scanSurroundings(trailhead)

