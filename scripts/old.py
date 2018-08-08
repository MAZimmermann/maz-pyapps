# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 12:11:49 2018

@author: MAZimmermann
"""

# Module for web scraping
from bs4 import BeautifulSoup

""""
 This is old code that I used for scraping Zacks and MarketWatch
 
 Keeping it here incase of future use
""""

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

"""
elif tickerInfo == "Alert Admin":
        return render_template('index.html') + render_template('scrapeBreak.html')
"""

""" Old styling for ohlc graph """
svg.append("text")
 .attr("transform", "translate("+(graphWidth+3)+","+y(graphData[0].High)+")")
 .attr("dy", "5%").attr("text-anchor", "start")
 .style("fill", "white")
 .text("Open");
svg.append("text")
 .attr("transform", "translate("+(graphWidth+3)+","+y(graphData[0].Low)+")")
 .attr("dy", "10%")
 .attr("text-anchor", "start")
 .style("fill", "green")
 .text("High");
svg.append("text")
 .attr("transform", "translate("+(graphWidth+3)+","+y(graphData[0].Close)+")")
 .attr("dy", "15%")
 .attr("text-anchor", "start")
 .style("fill", "red")
 .text("Low");
svg.append("text")
 .attr("transform", "translate("+(graphWidth+3)+","+y(graphData[0].Close)+")")
 .attr("dy", "20%")
 .attr("text-anchor", "start")
 .style("fill", "black")
 .text("Close");
 