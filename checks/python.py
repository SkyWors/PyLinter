from utils.get_lines import getLines
from tests.check_firstline import check_firstline
from tests.check_indentation import check_indentation
from tests.check_linebreak import check_linebreak
from tests.check_condition import check_condition

def checkPython(filePath):
	lines = getLines(filePath)

	i = 1
	for line in lines:
		if not line.replace("\t", "").startswith("#"):
			check_firstline(filePath, i, line)
			check_indentation(filePath, i, line)
			check_linebreak(filePath, i, line, lines)
			check_condition(filePath, i, line)
		i+=1
