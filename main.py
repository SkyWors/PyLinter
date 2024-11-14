from colorama import Fore, Style

filePath = "test/test.php"

with open(filePath, "r") as file:
	lines = []
	for line in file.readlines():
		lines.append(line)

def errorMessage(file, line, error):
	print(f"[{Fore.YELLOW}{file}{Style.RESET_ALL}] {Fore.CYAN}Line {line} {Style.RESET_ALL}| {Fore.RED}{error}{Style.RESET_ALL}")

i = 1
for line in lines:
	if not line.replace("\t", "").startswith("//"):
		# Check for first line
		if i == 1:
			if line == "\n":
				errorMessage(filePath, i, "File started with break line.")

		# Check for import format
		if "use" in line:
			if not "\"" in line:
				if line != "use\n":
					errorMessage(filePath, i, "Malformed use.")

		# Check for import format
		if lines[i-1] == "use\n":
			if not line.startswith("\t"):
				errorMessage(filePath, i, "Tabulations not found after use.")

		# Check for indentation
		if "    " in line:
			errorMessage(filePath, i, "Spaces instead of tabulations.")

		# Check for line break
		if line == "\n":
			if lines[i-2] == "\n":
				errorMessage(filePath, i, "Double line break.")

		# Check for if, while, for format
		if "if(" in line or "while(" in line or "for(" in line or "foreach(" in line:
			errorMessage(filePath, i, "Missing space before condition.")

		# Check for {}
		if line.replace("\t", "").startswith("{"):
			errorMessage(filePath, i, "Wtf this { do here?")

		# Check for ){
		if "){" in line:
			errorMessage(filePath, i, "Missing space after condition.")

	i+=1
