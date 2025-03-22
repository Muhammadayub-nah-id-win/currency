from os import getenv

import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = getenv('Your_API_Key')
async def currency_exchange(_from, _to):
    url = url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{_from}/{_to}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        kurs = data["conversion_rate"]
    return None


