# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 12:49:33 2018

@author: MAZimmermann
"""

import os
import datetime as dt
from datetime import timedelta
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime.now() + timedelta(-30)
end = dt.datetime.now()

# Creating new dataframe (basically a spreadsheet)
df = web.DataReader('TSLA', 'iex', start, end)

# Save our dataframe as a csv
df.to_csv('tsla.csv')

# LOTS of different I/O options with pandas
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# Delete 'tsla.csv' once we're done
os.unlink('tsla.csv')