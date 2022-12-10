from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from functools import lru_cache
from os import system
from os.path import basename, isfile
from platform import system as platform
from ping3 import ping
from requests import Session
from requests.adapters import HTTPAdapter
from time import perf_counter
from tqdm import tqdm
from urllib.parse import urlparse
from urllib.request import urlretrieve
from colorama import init, Fore

# Initialize the colorama module with autoreset enabled
init(autoreset=True)
