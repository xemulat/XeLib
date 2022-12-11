from colorama import Fore, init

# Initialize the colorama module with autoreset enabled
init(autoreset=True)

# Define a function that takes a string and a color number
# and returns the string with the specified color
def color(text, color):
    if color == 1:
        # Return the text with green color
        return(Fore.GREEN + text + Fore.RESET)

    elif color == 2:
        # Return the text with red color
        return(Fore.RED + text + Fore.RESET)

    elif color == 3:
        # Return the text with magenta color
        return(Fore.MAGENTA + text + Fore.RESET)

    elif color == 4:
        # Return the text with yellow color
        return(Fore.YELLOW + text + Fore.RESET)

    elif color == 5:
        # Return the text with blue color
        return(Fore.BLUE + text + Fore.RESET)
