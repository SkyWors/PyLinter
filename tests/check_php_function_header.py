from messages.error import errorMessage

def check_php_function_header(filePath, i, line):
	if "function (" in line:
		errorMessage(filePath, i, "Found space before arguments.")
