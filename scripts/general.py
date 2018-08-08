"""
 Author @MAZ
"""

# Module for web scraping
from bs4 import BeautifulSoup

# Module for making http requests
import requests

def generalInfo(appended):
    
    # Set ticker to whatever has been appended to the url
    ticker = appended

    # .upper() will change all the letters in 'ticker' to upercase (not sure if this is necessary)
    url = 'https://api.iextrading.com/1.0/stock/'+ticker.upper()+'/stats'
    
    # Make get request to our custom url, store response in resp
    resp = requests.get(url)
    
    """
    
    Additional library and code used for testing, no longer needed
    
    from requests_toolbelt.utils import dump
    
    data = dump.dump_all(resp)
    print(data.decode('utf-8'))
    
    """
    
    # This will prevent us from hitting a server error if an invalid ticker is used
    if "There were no matches found for" in resp.text:
        return "Invalid Ticker"
    elif "/tools/quotes/lookup.asp" in resp.text:
        return "Invalid Ticker"
    
    # Make new beautiful soup object
    soup = BeautifulSoup(resp.text, "lxml")
    
    # Set dataList to the bundle of elements/tags nested within class: 'list list--kv list--col50'
    dataList = soup.find('ul', {'class': 'list list--kv list--col50'})
    
    # Added for testing
    print(dataList)
    
    # This will prevent us from hitting a server error if a valid ticker is used, BUT
    #  MarketWatch has changed there html...
    if dataList is None:
        return "Alert Admin"
    
    stockInfo = []
    
    # Iterate through dataList and print dataListItem.text
    for dataListItem in dataList.findAll('li', {'class': 'kv__item'}):
        stockInfo.append(dataListItem.text)

    # Return list to be passed into our html template
    return stockInfo

"""
def pretty_print_POST(req):
    
    Helper function used for testing, no longer needed
    
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
"""

generalInfo('aapl')