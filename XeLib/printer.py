from colorama import init, Fore

# Initialize the colorama module with autoreset enabled
init(autoreset=True)

class printer:
    # Define a class method that takes a string and a color name
    # and prints the string with the specified color
    def cprint(cls, text, color):
        # Print the text with the specified color
        print(getattr(Fore, color.upper()) + text)

    # Define a class method that takes a string and prints it with blue color
    def blue(cls, text):
        print(Fore.BLUE + text)

    # Define a class method that takes a string and prints it with red color
    def red(cls, text):
        print(Fore.RED + text)

    # Define a class method that takes a string and prints it with red color
    # and a prefix of '[S>] '
    def lprint(cls, text):
        print(Fore.RED + '[S>] ' + text)
