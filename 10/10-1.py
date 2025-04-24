trailheadcoords = []
mapp = []
directions = []
tempdir = []
xcount = 0
ycount = 0
total = 0
trailtotal = 0

open("out.txt", "w").close()

def scanSurroundings(coords):
	global trailtotal
	global total
	global directions
	current = mapp[coords[0]][coords[1]]
	if current == 0:
		directions = []
		#with open("out.txt", "a") as f:
		#	f.write(','.join(str(x) for x in coords) + '\n')
		#	f.close()
	if current == 9:
		if coords not in directions:
			directions.append(coords)
			total += 1
		#with open("out.txt", "a") as f:
		#	f.write(' '.join(directions) + '\n')
		#	f.close()
		return
	else:
		target = current + 1
		if coords[0] - 1 >= 0:
			if target == mapp[coords[0]-1][coords[1]]:
				#tempdir = directions.copy()
				scanSurroundings([coords[0]-1, coords[1]])
				#directions = tempdir.copy()
		if coords[1] - 1 >= 0:
			if target == mapp[coords[0]][coords[1]-1]:
				#tempdir = directions.copy()
				scanSurroundings([coords[0], coords[1]-1])
				#directions = tempdir.copy()
		if coords[0] + 1 < ycount:
			if target == mapp[coords[0]+1][coords[1]]:
				#tempdir = directions.copy()
				scanSurroundings([coords[0]+1, coords[1]])
				#directions = tempdir.copy()
		if coords[1] + 1 < xcount:
			if target == mapp[coords[0]][coords[1]+1]:
				#tempdir = directions.copy()
				scanSurroundings([coords[0], coords[1]+1])
				#directions = tempdir.copy()

with open("input.txt", "r") as f:
	for line in f:
		linesplit = list(line)
		if '\n' in linesplit:
			linesplit.remove('\n')
		linesplit = list(map(int, linesplit))
		mapp.append(linesplit)

for line in mapp:
	xcount = 0
	for item in line:
		if item == 0:
			trailheadcoords.append([ycount, xcount])
		xcount += 1
	ycount += 1

for trailhead in trailheadcoords:
	scanSurroundings(trailhead)

print(total)