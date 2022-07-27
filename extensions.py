import requests
import json
from config import keys

class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convetr(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException('Необходимо указать две РАЗНЫЕ валюты')
        try:
            test = keys[quote]
        except KeyError:
            raise APIException(f'Такой валюты нет в списке конвертируемых {quote}')
        try:
            test = keys[base]
        except KeyError:
            raise APIException(f'Такой валюты нет в списке конвертируемых {base}')
        try:
            test = float(amount)
        except ValueError:
            raise APIException(f'Количество валюты указано не верно {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        t_base = json.loads(r.content)[keys[base]]
        return t_base
