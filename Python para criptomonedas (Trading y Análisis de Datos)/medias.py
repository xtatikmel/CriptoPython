import pandas as pd

df = pd.read_csv("ETHUSDT.csv")
# obtener los últimos 30 precios
last_30_prices = df["Close"].tail(360)
# calcular la media de los últimos 30 precios
mean_price = last_30_prices.mean()
# calcular la desviación estándar de los precios
std_price = last_30_prices.std()
# calcular los niveles de soporte y resistencia
support_price = mean_price - std_price
resistance_price = mean_price + std_price
# datos del último precio
last_price = df["Close"].iloc[-1]
# comparar el último precio con los niveles de soporte y resistencia
if last_price > resistance_price:
    status = "resistance"
    difference = last_price - resistance_price
elif last_price < support_price:
    status = "support"
    difference = support_price - last_price
else:
    status = "neutral"
    difference = 0
# 
print(f"The last price ({last_price}) is {status} with the difference {difference}.")
if status=="resistance":
    print("Send order to Sell")
elif status=="support":
    print("Send order Buy")
else:
    print("Hold/Or nothing")
