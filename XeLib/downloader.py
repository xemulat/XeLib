class downloader():
    def download(link, name, cmd):
        # REPORTER IS WORKING, DO NOT TOUCH IT
        def reporter(block_num, block_size, total_size):
            read_so_far = block_num * block_size
            if total_size > 0:
                percent = read_so_far * 1e2 / total_size
                print(
                    f"\r{percent:5.1f}% {read_so_far:{len(str(total_size))}} out of {total_size}", end='')
                if read_so_far >= total_size:
                    print()
            else:
                print(f"read {read_so_far}", end='')

        if cmd == False:
            print("Downloading " + name + " ...")
            urlretrieve(link, basename(urlparse(link).path), reporter)
            print(name + ' Downloaded!')
        else:
            print(Fore.RED + "[>] " + "Downloading " + name + " ...")
            urlretrieve(link, basename(urlparse(link).path), reporter)
            print(Fore.RED + "[>] " + name + ' Downloaded!')