import requests
import json
import time
from pymongo import MongoClient


# busca dados da API IBGE
url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
response = requests.get(url)
json_list = response.json()

# conecta na base
client = MongoClient('mongodb://localhost:27017/')
db = client.db
collection = db.distritos


# insere dados
try:
    start_time = time.time()
    for json_obj in json_list:
        json_dict = json.loads(json.dumps(json_obj))
        collection.insert_one(json_dict)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{len(json_list)} registros: tempo insert: {elapsed_time} secs")
except Exception as err:
    print(err)
