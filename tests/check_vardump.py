from messages.error import errorMessage

def check_vardump(filePath, i, line):
	if "var_dump" in line:
		errorMessage(filePath, i, "var_dump found.")
