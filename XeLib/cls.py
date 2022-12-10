from platform import system as platform
from os import system

# Define a function to clear the terminal screen
def cls():
    # Check the current platform
    if platform() == 'Windows':
        # Use the 'cls' command to clear the screen on Windows
        system('cls')
    else:
        # Use the 'clear' command to clear the screen on other platforms
        system('clear')
