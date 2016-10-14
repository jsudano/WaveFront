""" API Tester """

import CoOpsAPI.py

# TEST FUNCTIONS BELOW #

# Tests bad inputs
def testErrorHandling():
    print("Expected: 401 Error")
    a = CoOpsAPI("https://api.openweathermap.org/data/2.5/weather?q=London")
    a.checkStatus
    print("")

    print("Expected: Ambiguous Error")
    b = CoOpsAPI("a")
    a.checkStatus
    print("")

    print("Expected: Connection Failure")
    c = CoOpsAPI("http://a.com")
    c.checkStatus
    print("")



# TEST CALLS #

testErrorHandling()