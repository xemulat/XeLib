from colorama import init, Fore

# Initialize the colorama module with autoreset enabled
init(autoreset=True)

class printer:
    # Define a class method that takes a string and prints it with blue color
    def blue(text):
        print(Fore.BLUE + text)

    # Define a class method that takes a string and prints it with red color
    def red(text):
        print(Fore.RED + text)

    # Define a class method that takes a string and prints it with red color
    # and a prefix of '[S>] '
    def lprint(text):
        print(Fore.RED + '[S>] ' + text)