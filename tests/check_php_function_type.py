from messages.error import errorMessage

def check_php_function_type(filePath, i, line):
	if "function" in line:
		if "function\"" not in line:
			if ") :" in line:
				errorMessage(filePath, i, "Malformed function type.")
