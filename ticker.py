"""
 Author @MAZ
"""

# Module for web scraping
from bs4 import BeautifulSoup

# Module for making http requests
import requests

def grabTickerInfo(appended):
    # Set ticker to whatever has been appended to the url
    ticker = appended

    # .upper() will change all the letters in 'ticker' to upercase (not sure if this is necessary)
    url = 'https://www.marketwatch.com/investing/stock/'+ticker.upper()
    
    # Make get request to our custom url, store response in resp
    resp = requests.get(url)
    
    # Make new beautiful soup object
    soup = BeautifulSoup.BeautifulSoup(resp.text, "html.parser")
    
    # Set dataList to the bundle of elements/tags nested within class: 'list list--kv list--col50'
    dataList = soup.find('ul', {'class': 'list list--kv list--col50'})
    
    # Iterate through dataList and print dataListItem.text
    for dataListItem in dataList.findAll('li', {'class': 'kv__item'}):
        return dataListItem.text