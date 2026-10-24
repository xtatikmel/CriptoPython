import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FMP_API_KEY")
BASE_URL = "https://financialmodelingprep.com/stable"


def get_stock_quote(symbol):
    if not API_KEY:
        raise RuntimeError("No se encontró FMP_API_KEY en el archivo .env")

    response = requests.get(
        f"{BASE_URL}/quote",
        params={
            "symbol": symbol,
            "apikey": API_KEY,
        },
        timeout=30,
    )

    data = response.json()

    if response.status_code != 200:
        raise RuntimeError(f"Error HTTP de FMP: {response.status_code} - {data}")

    if isinstance(data, dict) and "Error Message" in data:
        raise RuntimeError(f"Error de FMP: {data['Error Message']}")

    if not data:
        raise RuntimeError(f"FMP no devolvió datos para {symbol}")

    return data[0]


quote = get_stock_quote("AAPL")

print("Symbol:", quote["symbol"])
print("Price:", quote["price"])
#print("Change %:", quote["changesPercentage"])
#print(quote["earningsAnnouncement"])