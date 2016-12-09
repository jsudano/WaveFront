""" API Tester """
from owmAPI import *
# TEST FUNCTIONS BELOW #

# Tests bad inputs
def testErrorHandling():
    try:
        a = owmAPI("111")
    except TypeError:
        return

def testSimpleSuccess():
    x = owmAPI((55.5, 37.5))
    str(x.Fetch())
    print(x.Fetch()['list'])

def testFloatLength():
    x = owmAPI((55.5, 37.5))
    if x.Fetch():
        print("SUCCESS")
    else:
        print("FAILURE")


# TEST CALLS #

#testErrorHandling()
#testSimpleSuccess()
testFloatLength()