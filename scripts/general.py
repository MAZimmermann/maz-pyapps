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
    url = 'https://www.marketwatch.com/investing/stock/'+ticker.upper()
    
    # Make get request to our custom url, store response in resp
    resp = requests.get(url)
    
    # This will prevent us from hitting a server error if an invalid ticker is used
    if "There were no matches found for" in resp.text:
        return 0
    elif "/tools/quotes/lookup.asp" in resp.text:
        return 0
    
    # Make new beautiful soup object
    soup = BeautifulSoup(resp.text, "html.parser")
    
    # Set dataList to the bundle of elements/tags nested within class: 'list list--kv list--col50'
    dataList = soup.find('ul', {'class': 'list list--kv list--col50'})
    
    # This will prevent us from hitting a server error if a valid ticker is used, BUT
    #  MarketWatch has changed there html...
    if dataList is None:
        return 1
    
    stockInfo = []
    
    # Iterate through dataList and print dataListItem.text
    for dataListItem in dataList.findAll('li', {'class': 'kv__item'}):
        stockInfo.append(dataListItem.text)

    # Return list to be passed into our html template
    return stockInfo

generalInfo('AAPL')