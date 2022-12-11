from ping3 import ping

def isinternet(website):
    # Ping the website
    pinged = ping(website, unit='ms')

    # Check if the ping was successful
    if pinged == False or pinged == None:
        return False
    else:
        return True