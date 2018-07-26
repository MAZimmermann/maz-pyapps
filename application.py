""" Author @MAZimmermann """

# Import Flask and render_template
from flask import Flask, render_template, request

# Import function I wrote in ticker.py
from ticker import grabTickerInfo

# Welcome message
def welcome():
    return render_template('index.html')

# This will validate the ticker appended by the user
def validateTicker(tick):
    tickerInfo = grabTickerInfo(tick)
    if tickerInfo == 0:
        return render_template('index.html') + render_template('errMsg.html', symbol=tick)
    else:
        return render_template('iter.html', info=tickerInfo, symbol=tick)

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
