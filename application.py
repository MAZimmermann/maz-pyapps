""" Author @MAZimmermann """

# Import Flask and render_template
from flask import Flask, render_template

# Import 'generalInfo' from general.py
from scripts.general import generalInfo

# Import 'ohlcInfo' from sma.py
from scripts.ohlc import ohlcInfo

# Welcome message
def welcome():
    return render_template('index.html')

# This will validate the ticker appended by the user
def validateTicker(tick):
    tickerInfo = generalInfo(tick)    
    if tickerInfo == "Invalid Ticker":
        return render_template('index.html') + render_template('invalidTicker.html', symbol=tick)
    else:
        lastMonth = ohlcInfo(tick)
        return render_template('ohlc.html', data=lastMonth, symbol=tick) + render_template('general.html', info=tickerInfo, symbol=tick)

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
