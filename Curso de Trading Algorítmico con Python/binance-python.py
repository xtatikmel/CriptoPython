from binance import Client
import pandas as pd
import datetime as dt
import mplfinance as mpl
#código para lanzar órdenes: https://stackoverflow.com/questions/66829757/how-to-create-buy-order-using-binance-api-on-python-using-all-my-selected-coin-i
api_key = key1 ("Aqui poneis la key entre comillas")
api_secret = key2 ("Aqui poneis la key entre comillas")
client = Client(api_key, api_secret)
price = client.get_symbol_ticker(symbol="ETHUSDT")
print(price)
#Practica con 10.000eur ficticios en: https://inversoresmilano.com/demo.html
asset="ETHUSDT"
start="2022.01.1"
end="2022.12.25"
timeframe="1d"
df= pd.DataFrame(client.get_historical_klines(asset, timeframe,start,end))
df=df.iloc[:,:6]
df.columns=["Date","Open","High","Low","Close","Volume"]
df=df.set_index("Date")
df.index=pd.to_datetime(df.index,unit="ms")
df=df.astype("float")
print(df)
import mplfinance as mpl
mpl.plot(df, type='candle', volume=True, mav=7)
#Si quieres el codigo para lanzar ordenes, mira este:
#https://stackoverflow.com/questions/66829757/how-to-create-buy-order-using-binance-api-on-python-using-all-my-selected-coin-i
