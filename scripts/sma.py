# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 12:49:33 2018

@author: MAZimmermann
"""

import os
import json
import datetime as dt
from datetime import timedelta
#import pandas as pd
#import pandas_datareader.data as web

def ohlcInfo():
    
    """start = dt.datetime.now() + timedelta(-30)
    end = dt.datetime.now()
    
    # Creating new dataframe (basically a spreadsheet)
    df = web.DataReader('TSLA', 'iex', start, end)
    
    # Save our dataframe as a csv
    df.to_csv('tsla.csv')
    
    # LOTS of different I/O options with pandas
    df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
    
    # Data that will be passed to application.py and rendered via an html template
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    
    # Delete 'tsla.csv' once we're done
    os.unlink('tsla.csv')
    
    return(data)"""