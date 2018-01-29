import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2013, 1, 1)
end = dt.datetime(2016, 12, 31)

df = web.DataReader('AAPL', "yahoo", start, end)

print(df.head())

keep_col = ['Open', 'High', 'Low', 'Volume', 'Close'] # except 'Date', 'Adj Close'
new_df = df[keep_col][:]
new_df.to_csv("inputs.csv", index=False, header=False)

