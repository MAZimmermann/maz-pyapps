"""
 Author @MAZ
"""

# Import Flask and render_template
from flask import Flask, render_template

# Import function I wrote in ticker.py
from ticker import grabTickerInfo

# Print welcome message
def welcome(ticker = " "):
    if ticker == " ":
        return render_template('index.html')
    else:
        return '<p>Company:<span style="color: red;"> %s </span></p>\n' % ticker.upper()

# This will validate the ticker appended by the user
def validateTicker(tick):
    tickerInfo = grabTickerInfo(tick)
    if tickerInfo == 0:
        errMsg = "This doesn't seem to be a valid ticker..."
        return errMsg
    else:
        return render_template('iter.html', info=tickerInfo)

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Add a rule for when simply accessing the index page
application.add_url_rule('/', 'index', (lambda: welcome()))

# Add a rule for when a ticker is appended to the url
application.add_url_rule('/<ticker>', 'hello', (lambda ticker: welcome(ticker) + validateTicker(ticker)))

# Run the app
if __name__ == "__main__":
    # Set debug to true for development/testing purposes
    application.debug = True
    application.run()
