from ping3 import ping

def isinternet(website):
    # Ping the website
    pinged = ping(website, unit='ms')

    # Check if the ping was successful
    if pinged == False:
        # Return "Unknown Host" if the website could not be resolved
        return "Unknown Host"
    if pinged == None:
        # Return "Timeout" if the ping request timed out
        return "Timeout"
    else:
        # Otherwise, return the ping time
        return "Ping - " + str(round(pinged, 2)) + "ms"
