"""Small class designed to handle the OpenWeatherMap.org API (Published at http://api.openweathermap.org/api/).
CO-OPS provides data from weather buoys accross the world. As far as I can tell, refresh rate is 6 minutes


***Note to Self***
Eventually, I should modularize the API class, because at its base they're both the same, and in the future
I plan on using multiple APIs. However, I'm in a rush to finish now, so this will do. 

"""

import requests

# Base API URL used to call with city ID (the most accurate means)
API_URL = "http://api.openweathermap.org/data/2.5/weather?id="

# Key linked to my personal account for openweathermap.org. Must be last string appended to request url
API_KEY = "&APPID=1c45f1223de502c389919db8eee5774e"

class owmAPI:
    def __init__(self, locID):
        self.locID = locID  # Locks the supplied location ID to the given class. Separate URLs need separate class instances
        self.refresh()

    # Requests data from source URL and location ID, sets it as various instance variables
    def refresh(self):
        try:
            self.data = requests.get(API_URL + self.locID + API_KEY)  # sets data variable to the requests Response object, returned by requests.get
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

    # Returns the requested data point
    def fetch(self, key):
        return self.json[key]

