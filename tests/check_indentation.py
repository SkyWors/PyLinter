from messages.error import errorMessage

def check_indentation(filePath, i, line):
	# Check for indentation
	if "    " in line:
		errorMessage(filePath, i, "Spaces instead of tabulations.")
