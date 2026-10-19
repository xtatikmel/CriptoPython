import pandas as pd
import numpy as np
# seleccionar CSV
xrp_df = pd.read_csv("XRPUSDT.csv").tail(30)
ada_df = pd.read_csv("ADAUSDT.csv").tail(30)
# columnas para el estudio
xrp_prices = xrp_df[["Date","Close"]]
ada_prices = ada_df[["Date","Close"]]
# combinar en un mismo dataframe
df = pd.merge(xrp_prices,ada_prices,on="Date",how="inner")
# correlación
correlation = np.corrcoef(df["Close_x"],df["Close_y"])[0,1]
print(correlation)

# asignar una puntuación basada en el nivel de correlación
if correlation > 0.8:
    score = 10
elif correlation > 0.78:
    score = 9
elif correlation > 0.4:
    score = 8
elif correlation > 0.2:
    score = 7
elif correlation > 0:
    score = 6
elif correlation > -0.2:
    score = 5
elif correlation > -0.4:
    score = 4
elif correlation > -0.6:
    score = 3
elif correlation > -0.8:
    score = 2
else:
    score = 1

# imprimir la puntuación
print(f"La puntuación de correlación entre xrp y ada es: {score}")