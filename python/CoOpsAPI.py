"""Small class designed to handle the CO-OPS API (Published at http://opendap.co-ops.nos.noaa.gov/ioos-dif-sos/#http-post).
CO-OPS provides data from weather buoys accross the world. As far as I can tell, refresh rate is 6 minutes
"""

import requests

class CoOpsAPI:

    def __init__(self, URL):
        self.URL = URL  # Locks the supplied URL to the given class. Separate URLs need separate class instances
        self.refresh()

    # Requests data from source URL, sets it as various instance variables
    def refresh(self):
        try:
            self.data = requests.get(self.URL)  # sets data variable to the requests Response object, returned by requests.get
            self.dataString = str(self.data.text)
            self.dataArray = self.dataString.split(",")  # Splits string into array of data points
            self.currentStatus = self.data.status_code
            return
        except requests.ConnectionError:
            print("A connection error occurred")
        except requests.HTTPError:
            print("An HTTP error occurred. Please review input URL")
        except requests.URLRequired:
            print("Please enter a valid URL")
        except requests.RequestException:
            print("Ambiguous connection error. Please review input URL")
        except requests.Timeout:
            print("Request timed out")
        self.currentStatus = -1  # Sets currentStatus so checkStatus can report a connection failure


    # Returns True if currentStatus contains status code 200, otherwise prints error codes and returns False
    def checkStatus(self):
        if (self.currentStatus == 200):
            return True
        elif (self.currentStatus == -1):
            print("An error occurred during connection, see console for details")
        else:
            eString = "Error Code {0}: ".format(self.currentStatus)
            print(eString + self.data.reason)  # Response.reason returns reason for error status
            return False


