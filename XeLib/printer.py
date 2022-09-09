from colorama import init, Fore
init(autoreset=True)

class printer:
    def cprint(text, color):
        print(Fore.color + text)

    def blue(text):
        print(Fore.BLUE + text)

    def red(text):
        print(Fore.RED + text)

    def lprint(text):
        print(Fore.RED + '[S>] ' + text)
