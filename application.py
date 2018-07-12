"""
 Author @MAZ
"""

# Import statement for flask
from flask import Flask

# Import statement for function I wrote in ticker.py
from ticker import grabTickerInfo

# Print a welcome message
def welcome(ticker = " "):
    if ticker == " ":
        return '<p>Welcome! Append a valid ticker symbol to the url and see what happens...</p>\n'
    else:
        return '<p>Company: %s </p>\n' % ticker

# Set title for webpage
header_text = '''<html>\n<head> <title>MAZ</title> </head>\n<body>'''

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    welcome()))

# Add a rule when the page is accessed with a ticker appended to the site
application.add_url_rule('/<ticker>', 'hello', (lambda ticker:
    header_text + welcome(ticker) + grabTickerInfo(ticker)))

# run the app.
if __name__ == "__main__":
    application.run()
