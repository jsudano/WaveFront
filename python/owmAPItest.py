""" API Tester """
from CoOpsAPI import *
# TEST FUNCTIONS BELOW #

# Tests bad inputs
def testErrorHandling():
    print("Expected: 401 Error")
    a = CoOpsAPI("http://api.openweathermap.org/data/2.5/weather?q=London")
    a.checkStatus()
    print("-----")

    print("Expected: Ambiguous Error")
    b = CoOpsAPI("a")
    b.checkStatus()
    print("-----")

    print("Expected: Connection Failure")
    c = CoOpsAPI("http://a.com")
    c.checkStatus()
    print("-----")



# TEST CALLS #

testErrorHandling()