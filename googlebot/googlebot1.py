#must have pytrends installed
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

print("debug 1")

pytrends.build_payload(kw_list=['coinbase'], timeframe='now 1-H')

print("debug 2")

testdata = pytrends.interest_over_time()

print("debug 3")

print(testdata)
