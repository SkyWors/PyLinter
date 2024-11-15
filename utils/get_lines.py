def getLines(filePath):
	with open(filePath, "r") as file:
		lines = []
		for line in file.readlines():
			lines.append(line)
	return lines
