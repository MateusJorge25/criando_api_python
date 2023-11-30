import requests         # Usa o requests para poder inserir o link da API
import json


cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()  # Serve para transformar o link acima em json
cotacoes_dolar = cotacoes['USDBRL'] ["bid"]         # Elementos usados para puxar a cotacao do dolar em tempo realz
print(cotacoes_dolar)





#print(cotacoes)   # A vareavel virou um dicionario


