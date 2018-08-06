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
    
    start = dt.datetime.now() + timedelta(-30)
    end = dt.datetime.now()
    
    ticker = appended.upper()
    
    # Creating new dataframe (basically a spreadsheet)
    df = web.DataReader(ticker, 'iex', start, end)
    
    filename = ticker + ".csv"
    
    # Save our dataframe as a csv
    df.to_csv(filename)
    
    # LOTS of different I/O options with pandas
    df = pd.read_csv(filename, parse_dates=True, index_col=0)
    
    print(df.head())
    
    # Data that will be passed to application.py and rendered via an html template
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    
    # Delete 'filename' once we're done
    os.unlink(filename)
    
    return(data)