import requests
import json
import time
import mysql.connector


def insere_registros(registros, qtd_execucoes):
    # conecta ao banco de dados mysql
    cnx = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='usuario',
        database='mysqldb'
    )
    cursor = cnx.cursor()

    # executa os inserts e calcula o tempo médio total
    tempo_total = 0
    for i in range(qtd_execucoes):
        try:
            start_time = time.time()
            for registro in registros:
                registro_json = json.dumps(registro)
                sql = "INSERT INTO DISTRITOS (distrito) VALUES (%s)"
                val = (registro_json,)
                cursor.execute(sql, val)
                cnx.commit()

            end_time = time.time()
            tempo_execucao = end_time - start_time
            tempo_total += tempo_execucao

            print(f"{len(registros)} registros (execução {i+1}/{qtd_execucoes}): tempo insert: {tempo_execucao} secs")
            
            # Limpa tabela
            cursor.execute("DELETE FROM DISTRITOS")
            cnx.commit()

        except Exception as err:
            print(err)

    #fecha conexão
    cursor.close()
    cnx.close()

    tempo_medio = tempo_total / qtd_execucoes
    print(f"Tempo médio para inserir {len(registros)} registros: {tempo_medio} segundos")


#quantidade de execuções e registros por teste
qtd_execucoes = 10
qtd_registros_tarefa = [100, 1000, 5000, 10000]

#busca dados da API de distritos do IBGE
url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
response = requests.get(url)
json_list = response.json()

#insere os registros para cada quantidade de registros na lista qtd_registros_tarefa
for qtd_registros in qtd_registros_tarefa:
    registros = json_list[:qtd_registros]
    insere_registros(registros, qtd_execucoes)