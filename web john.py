import pandas as pd
url = 'https://datos.trade/ccls'


# Esta linea lee a url, el [n] es la tabla de la pagina la que tiene la data
adr = pd.read_html(url, thousands=',', header=0)[0]
cedears= pd.read_html(url, thousands=',', header=0)[1]

list(cedears["Ticker"])


