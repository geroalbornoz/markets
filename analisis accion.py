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


adrs =[ ["BBAR",108.57,108.65,106.91],["BMA",107.96,108,106.91],["CEPU",105.09,105.49,106.91],["CRESY",105.35,105.68,106.91],["EDN",108.23,108.43,106.91],["GGAL",107.11,107.16,106.91],["PAM",108.32,108.35,106.91],["SUPV",105.66,105.68,106.91],["TEO",106.99,107.22,106.91],["TGS",104.77,105.03,106.91],["YPF",107.11,107.13,106.91]]

df1 = pd.DataFrame(adrs)