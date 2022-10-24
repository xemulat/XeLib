from colorama import Fore, init
init(autoreset=True)
def color(text, color):
    if color == 1:
        return(Fore.GREEN+text+Fore.WHITE)
    elif color == 2:
        return(Fore.RED+text+Fore.WHITE)
    elif color == 3:
        return(Fore.MAGENTA+text+Fore.WHITE)