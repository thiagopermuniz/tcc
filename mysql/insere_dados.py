import requests
import json
import time
import mysql.connector

# busca dados da API de distritos do IBGE
url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
response = requests.get(url)
json_list = response.json()

# conecta na base
cnx = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='usuario',
    database='mysqldb'
)
cursor = cnx.cursor()

# insere dados
try:
    start_time = time.time()
    for json_obj in json_list:
        json_str = json.dumps(json_obj)
        sql = "INSERT INTO DISTRITOS (distrito) VALUES (%s)"
        val = (json_str,)
        cursor.execute(sql, val)
        cnx.commit()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{len(json_list)} registros: tempo insert: {elapsed_time} secs")
# limpa tabela
    cursor.execute("DELETE FROM DISTRITOS")
    cnx.commit()
# fecha con
    cursor.close()
    cnx.close()

except Exception as err:
    print(err)

