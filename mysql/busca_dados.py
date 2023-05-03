import requests
import json
import time
import mysql.connector


def popula_banco_dados():
    # conecta ao banco de dados mysql
    cnx = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='usuario',
        database='mysqldb'
    )
    cursor = cnx.cursor()

    # busca dados da API de distritos do IBGE
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
    response = requests.get(url)
    json_list = response.json()

    try:
        # insere os registros na tabela de distritos
        for registro in json_list:
            registro_json = json.dumps(registro)
            sql = "INSERT INTO DISTRITOS (distrito) VALUES (%s)"
            val = (registro_json,)
            cursor.execute(sql, val)
            cnx.commit()
    except Exception as err:
        print(err)
    # fecha conexão
    cursor.close()
    cnx.close()


def busca_registros(qtd_execucoes, qtd_registros):
    # conecta ao banco de dados mysql
    cnx = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='usuario',
        database='mysqldb'
    )
    cursor = cnx.cursor()

    # executa as buscas e calcula o tempo médio total
    tempo_total = 0
    for i in range(qtd_execucoes):
        try:
            start_time = time.time()
            # executa a busca de registros na tabela
            sql = f"SELECT * FROM DISTRITOS LIMIT {qtd_registros}"
            cursor.execute(sql)
            result = cursor.fetchall()
            end_time = time.time()
            tempo_execucao = end_time - start_time
            tempo_total += tempo_execucao

            print(f"{len(result)} registros (execução {i+1}/{qtd_execucoes}): tempo de busca: {tempo_execucao} secs")
        except Exception as err:
            print(err)

    # fecha conexão
    cursor.close()
    cnx.close()

    tempo_medio = tempo_total / qtd_execucoes
    print(f"Tempo médio para buscar {len(result)} registros: {tempo_medio} segundos")


# quantidade de execuções e registros por teste
qtd_execucoes = 100
qtd_registros_tarefa = [100, 1000, 5000, 10000]

# popula a tabela de distritos com os dados da API do IBGE
popula_banco_dados()

# busca registros para cada quantidade de registros na lista qtd_registros_tarefa
for qtd_registros in qtd_registros_tarefa:
    busca_registros(qtd_execucoes, qtd_registros)