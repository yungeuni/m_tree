import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np

style.use('ggplot')

start = dt.datetime(2013, 1, 1)
end = dt.datetime(2016, 12, 31)

df = web.DataReader('012450.KS', "yahoo", start, end)

#print(df.head())

keep_col = ['Open', 'High', 'Low', 'Volume', 'Close'] # except 'Date', 'Adj Close'

new_df = df[keep_col][:]

new_df.to_csv("./data/inputs.csv", index=False, header=False)

print ("Shape: ", np.array(new_df).shape)

plt.plot(df['Close'][:])
plt.xlabel("Time Period")
plt.ylabel("Stock Price")
plt.show()


    