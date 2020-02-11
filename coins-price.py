import requests                             # Bibliotecas utilizadas.
import json
import time
import datetime


while True:                                 # Lopping para que o algoritmo atualize os calores das moedas.
    req = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,BTC-BRL,EUR-BRL')        # O request feito no site awasomeapi.
    cotacao = json.loads(req.text)

    print('=====COTAÇÃO=====')
    print('Data e hora:', datetime.datetime.now())          #Date time que informa o horário exato da cotação.
    print('Moeda:', cotacao ['USD'] ['name'])               #O nome da moeda.
    print('Valor:', cotacao ['USD'] ['high'])               #A cotação da moeda.
    print('-------------------------------')
    print('Moeda:', cotacao['BTC']['name'])
    print('Valor:', cotacao['BTC']['high'])
    print('-------------------------------')
    print('Moeda:', cotacao['EUR']['name'])
    print('Valor:', cotacao['EUR']['high'])
    print('-------------------------------')

    time.sleep(5)       # Time sleep para que o while se repita e atualize os numeros.




