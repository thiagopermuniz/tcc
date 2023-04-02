import requests
import json
import mysql.connector

# busca dados da API IBGE
url = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes"

response = requests.get(
    url, verify='/home/thiago/projects/tcc/mysql/ibge-gov-br.pem')

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

    json_obj = {"name": "John", "age": 30, "city": "New York"}
    json_str = json.dumps(json_obj)
    sql = "INSERT INTO tabela (json_data) VALUES (%s)"
    val = (json_str,)
    cursor.execute(sql, val)
    cnx.commit()
except Exception as err:
    print(err)
