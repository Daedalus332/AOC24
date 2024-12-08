import math
total = 0

with open("input.txt", "r") as f:
    doc = f.read()

with open("input1.txt", "w") as f:
    doc = doc.replace(")", ")\n")
    doc = doc.replace("]", "]\n")
    doc = doc.replace("$", "$\n")
    doc = doc.replace("!", "!\n")
    doc = doc.replace("#", "#\n")
    doc = doc.replace("[", "[\n")
    doc = doc.replace(";", ";\n")
    doc = doc.replace("-", "-\n")
    doc = doc.replace("}", "}\n")
    doc = doc.replace("<", "<\n")
    doc = doc.replace("~", "~\n")
    doc = doc.replace("*", "*\n")
    doc = doc.replace("?", "?\n")
    f.write(doc)


with open("input1.txt", "r") as f:
    for line in f:
        test = line[line.find("mul"):line.find(")")+1]
        if (len(test) <= 12 and len(test) > 3):
            otherstring = test[test.find("(")+1:test.find(")")]
            testlist = otherstring.split(",")
            try:
                list(map(int, testlist))
            except ValueError:
                continue
            testlist = list(map(int, testlist))
            total += math.prod(testlist)
            
print(total)
                    
                              
