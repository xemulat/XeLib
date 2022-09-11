from colorama import init, Fore
from os.path import basename, isfile, splitext
from urllib.request import urlretrieve
from urllib.parse import urlparse
from platform import system as platform
from ping3 import ping
from os import system
init(autoreset=True)