import requests
import json
import time
from pymongo import MongoClient


def insere_dados_mongodb(json_list, qtd_execucoes, tam_lista_registro):
    # conecta na base de dados
    client = MongoClient('mongodb://localhost:27017/')
    db = client.db
    collection = db.distritos

    total_time = 0
    # executa inserts e calcula tempo médio
    for i in range(qtd_execucoes):
        try:
            start_time = time.time()
            for json_obj in json_list[:tam_lista_registro]:
                json_dict = json.loads(json.dumps(json_obj))
                collection.insert_one(json_dict)
            end_time = time.time()
            elapsed_time = end_time - start_time
            total_time += elapsed_time
            print(f"{tam_lista_registro} registros (execução {i+1}/{qtd_execucoes}): tempo insert: {elapsed_time} secs")
            # limpa coleção
            collection.drop()
        except Exception as err:
            print(err)

    # fecha conexão com o banco de dados
    client.close()

    # calcula tempo médio
    media_tempo = total_time / qtd_execucoes
    print(f"Tempo médio para inserir {tam_lista_registro} registros: {media_tempo} segundos")


# quantidade de execuções e registros por teste
qtd_execucoes = 10
qtd_registros_tarefa = [10, 100, 1000, 10000]

# busca dados da API de distritos do IBGE
url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
response = requests.get(url)
json_list = response.json()

for tam_lista_registro in qtd_registros_tarefa:
    insere_dados_mongodb(json_list, qtd_execucoes, tam_lista_registro)
