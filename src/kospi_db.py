import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web
import datetime
import sqlite3

import os
for root, dirs, files in os.walk('./data/kospi-kosdaq-csv/kospi/'):
    for file in files:
		s = os.path.splitext(file)
		s = os.path.split(s[0])
		print s[1]

		path = './data/kospi-kosdaq-csv/kospi/{}.csv'.format(s[1])
		df = pd.read_csv(path)

		con = sqlite3.connect("kospi.db")
		df.to_sql(s[1], con, if_exists='replace')

'''
readed_df = pd.read_sql("SELECT * FROM s[1]", con, index_col = 'Date')


ticker = '067160'
path = './data/kospi-kosdaq-csv/kosdaq/{}.csv'.format(ticker)
df = pd.read_csv(path)

con = sqlite3.connect("kospi.db")
df.to_sql('067160', con, if_exists='replace')

readed_df = pd.read_sql("SELECT * FROM '067160'", con, index_col = 'Date')
'''

