#must have pytrends installed
from pytrends.request import TrendReq
import time


while True:
    pytrends = TrendReq(hl='en-US', tz=360)

#    print("debug 1")

    pytrends.build_payload(kw_list=['coinbase'], timeframe='now 1-H')

#    print("debug 2")

    testTime = pytrends.interest_over_time()

#    print("debug 3")

    print(testTime)

    testRegion = pytrends.interest_by_region(resolution='coinbase')

    print(testRegion)

    time.sleep(3)
