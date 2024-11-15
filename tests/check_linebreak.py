from messages.error import errorMessage

def check_linebreak(filePath, i, line, lines):
	if line == "\n":
		if lines[i-2] == "\n":
			errorMessage(filePath, i, "Double line break.")
