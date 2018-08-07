# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 12:49:33 2018

@author: MAZimmermann
"""

import os
import json
import datetime as dt
from datetime import timedelta
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

def ohlcInfo(appended):
    
    # Specify start and end date
    start = dt.datetime.now() + timedelta(-30)
    end = dt.datetime.now()
    
    # Grab the ticker appended to the url and make it uppercase (not sure if this is necessary...)
    ticker = appended.upper()
    
    # Creating new dataframe (basically a spreadsheet)
    df = web.DataReader(ticker, 'iex', start, end)
    
    filename = ticker
    
    # Save our dataframe as a csv
    df.to_csv(filename)
    
    # Read the newly saved csv and turn it into a pandas dataframe
    df = pd.read_csv(filename)
    
    # Data that will be passed to application.py and rendered via an html template
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    
    # Delete 'filename' once we're done
    os.unlink(filename)
    
    # Return data in dictionary format
    return(data)