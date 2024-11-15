from messages.error import errorMessage

def check_firstline(filePath, i, line):
	# Check for first line
	if i == 1:
		if line == "\n":
			errorMessage(filePath, i, "File started with break line.")
