# CriptoPython

Prácticas de trading algorítmico, criptomonedas, análisis financiero,
series temporales y visión artificial con Python. El repositorio contiene
scripts independientes y notebooks; no existe un único punto de entrada ni
un paquete instalable.

## Contenido

- `Curso de Trading Algorítmico con Python/`: indicadores, Binance, Yahoo
  Finance, MetaTrader 5 y modelos de clasificación.
- `Python para criptomonedas (Trading y Análisis de Datos)/`: extracción de
  datos, correlaciones y regresión.
- `Curso de Python para Finanzas y economía/`: manipulación de CSV/JSON,
  gráficos, MetaTrader 5 y Selenium.
- `Forecasting Crypto Portfolios Like a Quant/` y `Create a Cryptocurrency
  Trading Algorithm in Python/`: notebooks de forecasting.
- `Time Series Forecasting With Prophet/`: forecasting con Prophet.
- `OpenCV/`: ejercicios de visión artificial.

## Entorno y versiones

### Versiones verificadas en el repositorio

Las versiones de Python siguientes aparecen en la metadata de los notebooks:

| Componente | Versión | Uso |
| --- | --- | --- |
| Python | `3.11.5` | Notebooks actuales de forecasting, OpenCV y Prophet |
| Python | `3.7.12` | Notebooks históricos de forecasting |
| Kernel de Jupyter | `python3` | Notebooks con Python 3.11.5 |
| Kernel de Jupyter | `conda-env-python-py` | Notebooks con Python 3.7.12 |
| Sistema operativo documentado | Windows 10/11 | Comandos de esta guía |
| Shell | PowerShell | Ejemplos de ejecución |

El repositorio incluye `requirements.txt` en la raíz. Sus pins representan el
entorno consolidado del proyecto; deben validarse en Python `3.11.5` antes de
considerarlos un entorno certificado. No existen `Pipfile.lock`,
`poetry.lock`, `pyproject.toml`, `environment.yml` ni un archivo
`.python-version`. Las versiones históricas de algunas librerías no pueden
verificarse a partir del código fuente. Los imports usados en las prácticas
incluyen, entre otros:

- `numpy`, `pandas`, `matplotlib`, `seaborn`, `plotly` y `mplfinance`;
- `scikit-learn`, `statsmodels`, `pmdarima` y `prophet`;
- `yfinance`, `pandas-datareader`, `python-binance`, `requests` y
  `beautifulsoup4`;
- `opencv-python`, `selenium`, `webdriver-manager` y `MetaTrader5`.

`requirements.txt` funciona como lockfile de pip para este repositorio: cada
línea usa `==` y debe conservarse bajo control de versiones. Después de
instalar y ejecutar las prácticas en Python `3.11.5`, genere un backup
completo con `pip freeze` y revise cualquier diferencia antes de actualizar
el archivo.

## Instalación reproducible

Se recomienda usar Python `3.11.5` para las prácticas actuales. Mantenga
Python `3.7.12` únicamente para los notebooks históricos que lo requieren;
no mezcle ambos entornos.

### Opción A: entorno virtual de Python

Compruebe primero que el launcher de Python tenga la versión requerida:

```powershell
py -3.11 --version
```

Cree un entorno aislado e instale una versión fija de `pip`:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip==24.0
.\.venv\Scripts\python.exe -m pip install jupyter
```

Para el runtime histórico:

```powershell
py -3.7 -m venv .venv-py37
.\.venv-py37\Scripts\python.exe -m pip install --upgrade pip==23.2.1
```

### Opción B: entorno Conda para notebooks

Esta opción reproduce el tipo de kernel registrado en varios notebooks:

```powershell
conda create --name criptopython-py311 python=3.11.5 pip=24.0
conda activate criptopython-py311
python -m pip install jupyter ipykernel
python -m ipykernel install --user --name criptopython-py311 --display-name "Python (CriptoPython 3.11.5)"
```

Para los notebooks históricos:

```powershell
conda create --name criptopython-py37 python=3.7.12 pip=23.2.1
conda activate criptopython-py37
python -m pip install jupyter ipykernel
python -m ipykernel install --user --name criptopython-py37 --display-name "Python (CriptoPython 3.7.12)"
```

## Fijar y conservar dependencias

Un entorno virtual solo aísla instalaciones; no fija sus versiones. Para
evitar que una actualización futura cambie el resultado de las prácticas,
genere y confirme un `requirements.txt` después de instalar y validar todas
las librerías necesarias:

```powershell
.\.venv\Scripts\python.exe -m pip install <paquetes-validados>
.\.venv\Scripts\python.exe -m pip freeze --all | Set-Content -Encoding utf8 requirements.txt
```

El archivo debe contener entradas con versión exacta, por ejemplo
`paquete==1.2.3`, y debe revisarse junto con el código. Después de que
`requirements.txt` exista en el repositorio, las instalaciones reproducibles
deben usar `pip install`, nunca una resolución abierta con `pip install
<paquete>`:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip==24.0
.\.venv\Scripts\python.exe -m pip install --requirement requirements.txt
```

`pip freeze --all` captura el conjunto exacto instalado. En este proyecto,
`requirements.txt` es la opción más directa porque el stack detectado es
Python sin `pyproject.toml`. Si posteriormente se adopta Poetry, se deberán
versionar `pyproject.toml` y `poetry.lock`, y las instalaciones deberán
realizarse con `poetry install`. De forma equivalente, Pipenv requiere
versionar `Pipfile` y `Pipfile.lock`; no se deben mezclar gestores en el mismo
entorno.

No se debe regenerar `requirements.txt` durante una instalación normal. Solo
debe actualizarse de forma intencional, validando nuevamente los notebooks y
registrando el cambio.

## Ejecución

Active el entorno y abra Jupyter desde la raíz del repositorio:

```powershell
.\.venv\Scripts\Activate.ps1
python -m jupyter lab
```

También puede ejecutar un script concreto:

```powershell
.\.venv\Scripts\python.exe ".\Curso de Trading Algorítmico con Python\medias.py"
```

En cada notebook, seleccione el kernel correspondiente (`Python (CriptoPython
3.11.5)` o `Python (CriptoPython 3.7.12)`) antes de ejecutar las celdas.

## Requisitos externos y seguridad

- Las prácticas que consultan Binance, Yahoo Finance, Reddit u otros
  servicios requieren conexión a Internet y pueden cambiar por modificaciones
  de sus APIs.
- No escriba claves API, contraseñas ni tokens en los scripts o notebooks.
  Use variables de entorno y mantenga los valores fuera del control de
  versiones.
- Las operaciones de Binance deben probarse con testnet y credenciales
  limitadas antes de usar una cuenta real.
- Las prácticas de MetaTrader 5 requieren tener instalado el terminal de
  MetaTrader 5 y configurado el símbolo/cuenta correspondiente.
- La práctica de Selenium requiere Firefox y un driver compatible; revise la
  compatibilidad del navegador antes de ejecutar `webdriver-manager`.
- Los archivos CSV de datos incluidos son material de práctica y pueden tener
  fechas, precios o disponibilidad distintos de los servicios en línea.

## Estado de reproducibilidad

El lockfile de pip ya está presente en la raíz. La certificación final
requiere instalarlo y ejecutar las prácticas en Python `3.11.5`; el entorno
usado para generar la primera versión disponible fue Python `3.14.7`, por lo
que no debe confundirse el pinning con una validación funcional completa.
