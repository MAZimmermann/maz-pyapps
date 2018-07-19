"""
 Author @MAZ
"""

# Import statement for Flask and render_template
from flask import Flask, render_template

# Import statement for function I wrote in ticker.py
from ticker import grabTickerInfo

# Print a welcome message :)
def welcome(ticker = " "):
    if ticker == " ":
        return '<p>Welcome! Append a valid ticker symbol to the url for today\'s stats</p>\n'
    else:
        return '<p>Company: %s </p>\n' % ticker.upper()

# This validate the ticker appended by the user
def validTicker(tick):
    tickerInfo = grabTickerInfo(tick)
    if tickerInfo == 0:
        errMsg = "This doesn't seem to be a valid ticker..."
        return errMsg
    else:
        return render_template('iter.html', info=tickerInfo)

# Set title for webpage
header_text = '''<html>\n<head> <title>MAZ</title> </head>\n<body>'''

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Add a rule for when simply accessing the index page
application.add_url_rule('/', 'index', (lambda: header_text +
    welcome()))

# Add a rule for when a ticker is appended to the url
application.add_url_rule('/<ticker>', 'hello', (lambda ticker:
    header_text + welcome(ticker) + validTicker(ticker)))

# Run the app
if __name__ == "__main__":
    # Set debug to true for development/testing purposes
    application.debug = True
    application.run()
