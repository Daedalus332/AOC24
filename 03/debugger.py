linecount = 0

with open("input1.txt", "r") as f:
    for line in f:
        linecount += 1
        if line.count("mul") > 1:
            print(line)
