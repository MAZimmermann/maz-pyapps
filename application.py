""" Author @MAZimmermann """

# Import Flask and render_template
from flask import Flask, render_template, request

# Import 'generalInfo' from general.py
from scripts.general import generalInfo

# Import 'ohlcInfo' from sma.py
from scripts.sma import ohlcInfo

# Welcome message
def welcome():
    return render_template('index.html')

# This will validate the ticker appended by the user
def validateTicker(tick):
    tickerInfo = generalInfo(tick)    
    if tickerInfo == 0:
        return render_template('index.html') + render_template('invalidTicker.html', symbol=tick)
    elif tickerInfo == 1:
        lastMonth = ohlcInfo(tick)
        return render_template('index.html') + render_template('scrapeBreak.html') + render_template('sma.html', data=lastMonth)
    else:
        lastMonth = ohlcInfo(tick)
        return render_template('general.html', info=tickerInfo, symbol=tick) + render_template('sma.html', data=lastMonth)

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Add a rule for when simply accessing the index page
application.add_url_rule('/', 'index', (lambda: welcome()), methods=['GET', 'POST'])

# Add a rule for when a ticker is appended to the url
application.add_url_rule('/<ticker>', 'stats', (lambda ticker: validateTicker(ticker)), methods=['GET', 'POST'])

# Run the app
if __name__ == "__main__":
    # Set debug to true for development/testing purposes
    application.debug = True
    application.run()
