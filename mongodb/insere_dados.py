import requests
import json
import time
from pymongo import MongoClient


# busca dados da API IBGE
url = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes"
response = requests.get(url)
json_list = response.json()

# conecta na base
client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
collection = db.mycollection


# insere dados
try:
    start_time = time.time()
    for json_obj in json_list:
        json_str = json.dumps(json_obj)
        collection.insert_one(json_str)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"tempo insert: {elapsed_time} secs")
except Exception as err:
    print(err)
