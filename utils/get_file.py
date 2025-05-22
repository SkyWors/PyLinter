import os
import sys
from checks.php import checkPHP
from checks.js import checkJS
from checks.python import checkPython

def getFile(path, excludeFolder):
	if os.path.isdir(path):
		if path.replace(sys.argv[1] + "/", "") not in excludeFolder:
			for file in os.listdir(path):
				if not file.startswith(".") and not file.startswith("_"):
					getFile(path + "/" + file, excludeFolder)
	else:
		if ".php" in path:
			checkPHP(path)
		if ".js" in path:
			if ".json" not in path:
				if ".min." not in path:
					checkJS(path)
		if ".py" in path:
			checkPython(path)
