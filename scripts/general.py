"""
 Author @MAZ
"""

import json

# Module for making http requests
import requests

def generalInfo(appended):
    
    # Set ticker to whatever has been appended to the url
    ticker = appended

    # .upper() will change all the letters in 'ticker' to upercase (not sure if this is necessary)
    url = 'https://api.iextrading.com/1.0/stock/'+ticker.upper()+'/stats'
    
    # Make get request to our custom url, store response in resp
    resp = requests.get(url)
    
    json_data = json.loads(resp.text)
    
    stockInfo = []
    
    for item in json_data:
        stockInfo.append(item + ": " + str(json_data[item]))
    
    """
    
    Additional library and code used for testing, no longer needed
    
    from requests_toolbelt.utils import dump
    
    data = dump.dump_all(resp)
    print(data.decode('utf-8'))
    
    """
    
    return stockInfo