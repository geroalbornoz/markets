import requests
import pandas as pd
import datetime as dt
import mplfinance as fplt
import matplotlib.pyplot as plt

def getData():
    url = 'https://pro-data.trademaster.com.ar/tv/history?symbol=ROFX%3ARFX20Sep20&resolution=1m&from=1598459023&to=1598459631'
    #url = 'https://pro-data.trademaster.com.ar/tv/history?symbol=ROFX%3ARFX20Sep20&resolution=1&from=1598360400&to=1598385600'
    r = requests.get(url)
    data =  r.json()
    trades = pd.DataFrame(data=data, columns=['o','h','l','c','v','t'])
    trades ['hora'] = pd.to_datetime(trades.t, unit='s')
    trades.set_index('hora', inplace=True)
   
    return pd.DataFrame(data=trades)
  
trades = getData()
print(trades.v.sum())
print(trades)
fplt.plot(trades, type='candle')
