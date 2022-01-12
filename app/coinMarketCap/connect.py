 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import threading
import time

url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
parameters = {
  # 'start':'1',
  # 'limit':'5000',
  # 'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '9c6b7d4a-28b8-4d53-8089-db4c96b6c088',
}

session = Session()
session.headers.update(headers)

def getGlobalMetrics(): 
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
  return data

def getBTCDominance():
  try:
    data = getGlobalMetrics()
    #print(data)
    btcDominance = data['data']['btc_dominance']
    print("Bitcoin Dominance: " + str(btcDominance))
    return btcDominance

  except (BaseException) as e:
    print(e)  

# # This function will be started in it's own thread
# def funcloop(func, sleeptime, *args, **kwargs):
#     while True:
#         func(*args, **kwargs)
#         time.sleep(sleeptime)

# getBTCDominance()
# threading.Timer(60,getBTCDominance).start() 