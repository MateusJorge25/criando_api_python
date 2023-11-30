import requests
import json 

uf = str(input("Digite o UF:"))

cidade = str(input("Digite o nome da cidade:"))

logradouro = str(input("Digite o logradouro:"))


local = requests.get(f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/")
local = local.json()
print(local)