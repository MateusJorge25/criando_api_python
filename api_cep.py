import requests
import json


cep = int(input("Digite seu cep:"))



local = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
local = local.json()
print(local)



