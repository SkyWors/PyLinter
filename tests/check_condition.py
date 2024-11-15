from messages.error import errorMessage

def check_condition(filePath, i, line):
	# Check for if, while, for format
	if "if(" in line or "while(" in line or "for(" in line or "foreach(" in line:
		errorMessage(filePath, i, "Missing space before condition.")

	# Check for {}
	if line.replace("\t", "").startswith("{"):
		errorMessage(filePath, i, "Wtf this { do here?")

	# Check for ){
	if "){" in line:
		errorMessage(filePath, i, "Missing space after condition.")
