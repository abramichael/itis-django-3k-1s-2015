f = open("input.txt")
g = open("output.txt", "w")

for line in f:
    line = line.strip()
	
	#... changing line somehow
	
    g.write(line + "\n")

g.close()