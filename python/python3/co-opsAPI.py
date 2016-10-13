"""Small class designed to handle the CO-OPS API (Published at http://opendap.co-ops.nos.noaa.gov/ioos-dif-sos/#http-post).
CO-OPS provides data from weather buoys accross the world. As far as I can tell, refresh rate is 6 minutes
"""

import requests

class CoopsAPI:

    def __init__(URL):
        self.URL = URL  # Locks the supplied URL to the given class. Separate URLs need separate class instances
        refresh()

    def refresh():
        self.data = requests.get(URL)  # sets data variable to the requests Response object, returned by requests.get
        self.dataString = str(data.text)
        self.dataArray = dataString.split(",")  # Splits string into array of data points
        self.currentStatus = data.status_code

    # Returns True if currentStatus contains status code 200, otherwise prints error codes and returns False
    def checkStatus():
        if (self.currentStatus == 200):
            return True
        else:
            eString = "Error Code: {0}".format(currentStatus)
            print(eString + data.reason)  # Response.reason returns reason for error status
            return False

