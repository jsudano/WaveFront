"""Small class designed to handle the OpenWeatherMap.org API (Published at http://api.openweathermap.org/api/).
CO-OPS provides data from weather buoys accross the world. As far as I can tell, refresh rate is 6 minutes

"""

import requests

# Base API URL used to call with city ID (the most accurate means)
API_URL = "http://api.openweathermap.org/data/2.5/find?"
CNT_URL = "&cnt=50"

# Key linked to my personal account for openweathermap.org. Must be last string appended to request url
API_KEY = "&APPID=1c45f1223de502c389919db8eee5774e"

class owmAPI:
    def __init__(self, coords):
        self.coords = coords  # Locks the supplied coordinates to the given class. Separate URLs need separate class instances
        if (isinstance(coords, tuple)) and (isinstance(coords[0], float)):
            self.refresh()
        else:
            raise TypeError("Malformed input, expected tuple of floats")

    # Requests data from source URL and location ID, sets it as various instance variables
    def refresh(self):
        try:
            # sets data variable to the requests Response object, returned by requests.get
            self.data = requests.get(API_URL + 
                                    "lat=" + str(self.coords[0]) +
                                    "&lon=" + str(self.coords[1]) +
                                    CNT_URL + 
                                    API_KEY) 
            self.json = self.data.json() # Thank god requests has a built in JSON decoder. Returns a dict
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
        self.currentStatus = -1  # Sets currentStatus so checkStatus can report 


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

    # Returns the requested data as a json dict, or -1 if request failed
    def Fetch(self):
        if(self.checkStatus):
            return self.json
        return -1

