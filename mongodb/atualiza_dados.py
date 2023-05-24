import requests
import json
import time
from pymongo import MongoClient


def popula_banco_dados():
    # ... existing code for populating the database ...


def busca_registros(qtd_execucoes, qtd_registros):
    # ... existing code for querying records ...


def atualiza_registros(qtd_execucoes, qtd_registros):
    # Connect to the MongoDB database
    client = MongoClient('mongodb://localhost:27017/')
    db = client.db
    collection = db.distritos

    # Execute the updates and calculate the total average time
    tempo_total = 0
    for i in range(qtd_execucoes):
        try:
            start_time = time.time()

            # Execute the update on records in the collection
            # For example, let's update the 'nome' field of the first 'qtd_registros' records
            for registro in collection.find().limit(qtd_registros):
                registro['nome'] = 'New Name'
                collection.replace_one({'_id': registro['_id']}, registro)

            end_time = time.time()
            tempo_execucao = end_time - start_time
            tempo_total += tempo_execucao

            print(f"{qtd_registros} registros (execução {i+1}/{qtd_execucoes}): tempo de atualização: {tempo_execucao} segundos")

        except Exception as err:
            print(err)

    # Close the connection
    client.close()

    tempo_medio = tempo_total / qtd_execucoes
    print(f"Tempo médio para atualizar {qtd_registros} registros: {tempo_medio} segundos")


# quantidade de execuções e registros por teste
qtd_execucoes = 100
qtd_registros_tarefa = [100, 1000, 5000, 10000]

# popula a coleção de distritos com os dados da API do IBGE
popula_banco_dados()

# busca registros para cada quantidade de registros na lista qtd_registros_tarefa
for qtd_registros in qtd_registros_tarefa:
    busca_registros(qtd_execucoes, qtd_registros)

# atualiza registros para cada quantidade de registros na lista qtd_registros_tarefa
for qtd_registros in qtd_registros_tarefa:
    atualiza_registros(qtd_execucoes, qtd_registros)