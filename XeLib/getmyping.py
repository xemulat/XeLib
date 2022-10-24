from colorama import Fore, init
from ping3 import ping
init(autoreset=True)
def getmyping():
    if ping("github.com") == False or None:
        return(Fore.RED+"None")
    else:
        peng = (str(ping("github.com", unit='ms')).split(".", 1)[0])
        return(Fore.GREEN+peng + "ms")