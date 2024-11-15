import sys
from colorama import Fore, Style
from utils.get_file import getFile

if __name__ == "__main__":
	excludeFolder = ["vendor"]
	getFile(sys.argv[1], excludeFolder)

	print(f"{Fore.GREEN}All tests done.{Style.RESET_ALL}")
