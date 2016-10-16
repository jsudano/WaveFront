""" API Tester """
from owmAPI import *
# TEST FUNCTIONS BELOW #

# Tests bad inputs
def testErrorHandling():
    print("Expected: 401 Error")
    a = owmAPI("111")
    a.checkStatus()
    print("-----")

    print("Expected: Ambiguous Error")
    b = owmAPI("a")
    b.checkStatus()
    print("-----")

    print("Expected: Connection Failure")
    c = owmAPI("http://a.com")
    c.checkStatus()
    print("-----")

def testSimpleSuccess():
    print("Expected Array of weather data")
    x = owmAPI("524901")
    print(str(x.fetch("message")))


# TEST CALLS #

testErrorHandling()
testSimpleSuccess()