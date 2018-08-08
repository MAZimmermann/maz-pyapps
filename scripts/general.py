"""
 Author @MAZ
"""

# Module for handling json representation
import json

# Module for making http requests
import requests

# Hope to utilize this in the near future, keys in the json object are concatenated
# import nltk

def generalInfo(appended):
    
    # Set ticker to whatever has been appended to the url
    ticker = appended

    # .upper() will change all the letters in 'ticker' to upercase (not sure if this is necessary)
    url = 'https://api.iextrading.com/1.0/stock/'+ticker.upper()+'/stats'
    
    # Make get request to our custom url, store response in resp
    resp = requests.get(url)
    
    if 'Unknown symbol' in str(resp.content):
        return "Invalid Ticker"
    
    # Turn response into json objecy
    json_data = json.loads(resp.text)
    
    # Define/Initialize string array to be passed to general.html template
    stockInfo = []
    
    # Iterate throguh json object, special instructions needed for each key
    for item in json_data:
        # print(nltk.word_tokenize(item))
        stockInfo.append(item + ": " + str(json_data[item]))
    
    """
    
    Additional library and code used for testing, no longer needed
    
    from requests_toolbelt.utils import dump
    
    data = dump.dump_all(resp)
    print(data.decode('utf-8'))
    
    """
    
    # Return stockInfo[]
    return stockInfo