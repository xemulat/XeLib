from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from os.path import isfile
from time import perf_counter
from urllib.parse import urlparse
from requests import Session
from requests.adapters import HTTPAdapter

from functools import lru_cache
from colorama import Fore, init
from tqdm import tqdm

init(autoreset=True)

def download(link, fnam, name):
    @lru_cache(maxsize=None)
    def download(link, fnam, name):
        # Check if the file specified by 'fnam' already exists on the file system.
        if isfile(fnam) == False:

            start_time = perf_counter()

            # Parse the URL and convert it to https.
            link = (urlparse(link))._replace(scheme='https').geturl()

            print(Fore.RED + f'[>] Downloading {name}...')

            # Configure an HTTP adapter with retries and connection pooling.
            adapter = HTTPAdapter(max_retries=3,
                                  pool_connections=20,
                                  pool_maxsize=10)

            # Set some headers for the request.
            headers = {'Accept-Encoding': 'gzip, deflate',
                       'User-Agent': 'Mozilla/5.0',
                       'cache_control': 'max-age=600',
                       'connection': 'keep-alive'}

            # Create a new session for the request.
            session = Session()

            # Mount the HTTP adapter to the session.
            session.mount('https://', adapter)

            # Use a context manager to download the file and display the progress.
            with closing(session.get(link,
                                    allow_redirects=True,
                                    stream=True,
                                    headers=headers)) as r:

                # Get the total size of the file.
                total_size = int(r.headers.get('content-length', 0))
                block_size = 4096 # 4 Kibibytes

                # Create a progress bar to display the download progress.
                progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

                # Open the file for writing and download the file in chunks.
                with open(fnam, 'wb') as file:
                    for data in r.iter_content(block_size):
                        progress_bar.update(len(data))
                        file.write(data)

                # Close the progress bar and print a message when the download is complete.
                progress_bar.close()
                download_time = perf_counter() - start_time
                print(Fore.RED + f'[>] {name} Downloaded in {round(download_time)}s!')

        # If the file already exists, print a message.
        else:
            print(Fore.RED + f"[>] {name} is already downloaded...")

    with ThreadPoolExecutor() as executor:
        executor.submit(download, link, fnam, name)