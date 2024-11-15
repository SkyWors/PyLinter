from messages.error import errorMessage

def check_php_import(filePath, i, line, lines):
	# Check for import format
	if "use" in line:
		if not "\"" in line:
			if line != "use\n":
				errorMessage(filePath, i, "Malformed use.")

	# Check for import format
	if lines[i-1] == "use\n":
		if not line.startswith("\t"):
			errorMessage(filePath, i, "Tabulations not found after use.")
