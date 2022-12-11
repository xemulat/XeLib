from colorama import Fore, init
from ping3 import ping

# Initialize the colorama module with autoreset enabled
init(autoreset=True)

def getmyping():
    # Check if the ping to github.com is successful
    if ping("github.com") == False or None:
        # Return "None" with red color if the ping failed
        return("None")
    else:
        # Otherwise, get the ping time and return it with green color
        peng = (str(ping("github.com", unit='ms')).split(".", 1)[0])
        return(peng + "ms")