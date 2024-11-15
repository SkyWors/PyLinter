from colorama import Fore, Style

def errorMessage(file, line, error):
	print(f"[{Fore.YELLOW}{file}{Style.RESET_ALL}] {Fore.CYAN}Line {line} {Style.RESET_ALL}| {Fore.RED}{error}{Style.RESET_ALL}")
