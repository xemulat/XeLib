from urllib.request import urlretrieve
from colorama import init, Fore
init(autoreset=True)

def download(link, fnam, name):
    def reporter(block_num, block_size, total_size):
        read_so_far = int(str((block_num * block_size) / 1024).split(".", 1)[0])
        total_size = int(str(total_size / 1024).split(".", 1)[0])
        if total_size > 0:
            percent = read_so_far * 1e2 / total_size
            print(f"\r{percent:5.1f}% {read_so_far:{len(str(total_size))}} out of {total_size}kb", end='')
            if read_so_far >= total_size:
                print()
        else:
            print(f"read {read_so_far}", end='')

    if not "https://" in link:
        link = "https://" + link
    print(Fore.RED + "[>] " + "Downloading " + name + " ...")
    urlretrieve(link, fnam, reporter)
    print(Fore.RED + "[>] " + name + ' Downloaded!')