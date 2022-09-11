from ping3 import ping

def isinternet(website):
    pinged = ping(website, unit='ms')
    if pinged == False:
        return "Unknown Host"
    if pinged == None:
        return "Timeout"
    else:
        return "Ping - " + str(round(pinged, 2)) + "ms"