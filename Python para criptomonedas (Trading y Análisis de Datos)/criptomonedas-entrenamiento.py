import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Cargar datos
btc_data = pd.read_csv("BTCUSDT.csv").tail(30)
eth_data = pd.read_csv("ETHUSDT.csv").tail(30)

# Preprocesamiento
btc_data.dropna(inplace=True)
eth_data.dropna(inplace=True)

# Desplazar un día la columna "Close" de "BTCUSDT.csv"
btc_data['Close'] = btc_data['Close'].shift(1)

#Combinar los dos dataframes usando la columna "Date"
merged_data = pd.merge(btc_data[['Date', 'Close']], eth_data[['Date', 'Close']], on='Date', how='inner')

# Dividir los datos en conjuntos de entrenamiento y prueba
train_data = merged_data.iloc[:-1, :]
test_data = merged_data.iloc[-1:, :]

# Imputar los valores faltantes usando la media
imputer = SimpleImputer(strategy='mean')
train_predictors = imputer.fit_transform(train_data.iloc[:, 1].values.reshape(-1, 1))
test_predictors = imputer.transform(test_data.iloc[:, 1].values.reshape(-1, 1))

# Ajustar el modelo de regresión lineal
regression = LinearRegression()
regression.fit(train_predictors, train_data.iloc[:, 2].values.reshape(-1, 1))

# Predecir el precio de cierre de "ETHUSDT.csv"
predicted_price = regression.predict(test_predictors)

# Comprobar si el precio va a subir o bajar
if predicted_price > test_data.iloc[0, 2]:
    print("The price of ETHUSDT is predicted to go up.")
    
else:
    print("The price of ETHUSDT is predicted to go down.")