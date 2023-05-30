import requests
import json
import time
from pymongo import MongoClient


def popula_banco_dados():
    # conecta ao banco de dados mongodb
    client = MongoClient('mongodb://localhost:27017/')
    db = client.db
    collection = db.distritos

    # busca dados da API de distritos do IBGE
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
    response = requests.get(url)
    json_list = response.json()

    try:
        # insere os registros na coleção de distritos
        for registro in json_list:
            collection.insert_one(registro)
    except Exception as err:
        print(err)

    # fecha conexão
    client.close()


def atualiza_registros(qtd_execucoes, qtd_registros):
    # conecta ao banco de dados mysql
    client = MongoClient('mongodb://localhost:27017/')
    db = client.db
    collection = db.distritos

    # executa as atualizações e mede o tempo
    tempo_total = 0
    for i in range(qtd_execucoes):
        try:
            start_time = time.time()

            for registro in collection.find().limit(qtd_registros):
                registro['nome'] = 'Novo Nome Distrito'
                registro['municipio']['nome'] = 'Novo Nome Municipio'
                registro['municipio']['microrregiao']['nome'] = 'Novo Nome Microregiao'
                collection.replace_one({'_id': registro['_id']}, registro)

            end_time = time.time()
            tempo_execucao = end_time - start_time
            tempo_total += tempo_execucao

            print(f"{qtd_registros} registros (execução {i+1}/{qtd_execucoes}): tempo de atualização: {tempo_execucao} segundos")

        except Exception as err:
            print(err)

    # fecha a conexão com o banco de dados
    client.close()

    tempo_medio = tempo_total / qtd_execucoes
    print(f"Tempo médio para atualizar {qtd_registros} registros: {tempo_medio} segundos")


# quantidade de execuções e registros por teste
qtd_execucoes = 100
qtd_registros_tarefa = [10, 100, 1000, 10000]

# popula a coleção de distritos com os dados da API do IBGE
popula_banco_dados()


# atualiza registros para cada quantidade de registros na lista qtd_registros_tarefa
for qtd_registros in qtd_registros_tarefa:
    atualiza_registros(qtd_execucoes, qtd_registros)