import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt



ticker = "GGAL.BA"
data = yf.download(ticker, period='20y')
print('\n--Describe--\n', data.describe())
print('\n--Head--\n', data.head(4))
print('\n--Columns--\n', data.columns)

plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = [12.0, 5]

variaciones =  data['Adj Close'].pct_change()*100
agrupados = variaciones.groupby(data.index.year).sum()
agrupados.plot(kind='bar',title='Rendimientos GGAL USD')
plt.show()

plt.style.use('dark_background')
variaciones =  data['Adj Close'].pct_change()*100
agrupados = variaciones.groupby(data.index.dayofweek).mean()
agrupados.plot(kind='bar',title='Rendimientos GGAL USD')
plt.show()

#RESAMPLE
data['Adj Close'].resample('W').last() 
variaciones =  data['Adj Close'].pct_change()*100
agrupados = variaciones.groupby(data.index.week).mean()
agrupados.plot(kind='bar',title='Rendimientos GGAL USD')
plt.show()

data['Adj Close'].resample('M').last() 
variaciones =  data['Adj Close'].pct_change()*100
agrupados = variaciones.groupby(data.index.month).mean()
agrupados.plot(kind='bar',title='Rendimientos GGAL USD')

variaciones.head()


