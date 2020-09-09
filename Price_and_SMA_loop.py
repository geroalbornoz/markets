import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
import plotly.express as px
plt.rcParams['figure.figsize'] = (19,9)

api_key ="F7JZ1R3NFA6BNMRR"

cedears = ['AAPL',
 'ABEV',
 'ABT',
 'AIG',
 'AMD',
 'AMX',
 'AMZN',
 'ARCO',
 'AUY',
 'AXP',
 'BA',
 'BA.C',
 'BABA',
 'BBD',
 'BCS',
 'BIDU',
 'BP',
 'BSBR',
 'C',
 'CHL',
 'CSCO',
 'CVX',
 'DESP',
 'DIS',
 'EBAY',
 'ERJ',
 'FB',
 'FCX',
 'FMX',
 'GE',
 'GOLD',
 'GOOGL',
 'GSK',
 'HD',
 'HMY',
 'HPQ',
 'HSBC',
 'IBM',
 'INTC',
 'ITUB',
 'JD',
 'JNJ',
 'JPM',
 'KO',
 'LVS',
 'MCD',
 'MELI',
 'MMM',
 'MO',
 'MSFT',
 'NFLX',
 'NKE',
 'NOKA',
 'PBR',
 'PFE',
 'PYPL',
 'QCOM',
 'SID',
 'SNAP',
 'SUZ',
 'T',
 'TEN',
 'TOT',
 'TSLA',
 'TSU',
 'TWTR',
 'V',
 'VALE',
 'WFC',
 'WMT',
 'X',
 'XOM']

period =200

symbol=['AAPL',
 'GOLD',
 'MELI',
 'MSFT',
 'BAC',
 ]

ti = TechIndicators(key=api_key, output_format="pandas") #para pedir los indicadores a esta variable
ts = TimeSeries(key=api_key, output_format="pandas") #para pedir la info usaremos esta variable


print("descargando precios de cierre Cedears")


for cedear in cedears:
    data, meta_data = ts.get_daily(symbol=symbol,outputsize="full") #abajamos los precios diarios
    data_ti, meta_data_ti = ti.get_sma(symbol=symbol, interval="daily", time_period= period,
                                       series_type="close") #abajamos el calculo de media movil simple
    data_source= str(cedear)+".csv"
    print(str(cedear)+" listo")




df1 = data_ti
df2 = data["4. close"].iloc[period-1::] 

#le sacamos las 2ras 20 filas al df2 del precio cierre para igualarlo al  de SMA


df2.index=df1.index

total_df = pd.concat([df1,df2],axis=1) #JUNTAMOS AMBOS DF 


#acá armamos un gráfico que muestre el precio y la SMA 30 (stan weinstein)


total_df.plot()
plt.title(symbol+ " - " + "Precio Cierre y SMA"+str(period))
plt.show()


print("listo Gráficos precios de cierre Cedears vs. SMA")

#data["pct_change"] = close_data.pct_change() #agrego una columna de variacion de precio %
#SMA_data = close_data.rolling(window=30).mean() #para calcular la media con pandas
