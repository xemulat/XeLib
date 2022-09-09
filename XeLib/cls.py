from platform import system as platform
from os import system

def cls():
    if platform() == 'Windows':
        system('cls')
    else:
        system('clear')
