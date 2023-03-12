import pandas as pd
import sys
import json
import mysql.connector
from pymongo import MongoClient


DATABASE = sys.argv[1] # 'mongodb' ou 'mysql'
FILE = sys.argv[2] # local do arquivo xlsx
#Exemplo de exec:  "$ python.exe popula_database.py mongodb base-teste.xlsx"
print('base selecionada: ' + DATABASE)

# lê arquivo excel (xlsx)
df = pd.read_excel(FILE)

# conecta na base
try:
    if DATABASE == 'mysql':
        cnx = mysql.connector.connect(user='usuario', host='localhost', database='base-tcc')
        cursor = cnx.cursor()
    elif DATABASE == 'mongodb':
        client = MongoClient('mongodb://localhost:27017/')
        db = client.mydb
        collection = db.mycollection
except Exception as err:
    print(f"falha ao conectar na base de dados: {err}") 

# insere dados
try:
    while True:
        for index, row in df.iterrows():
            document = {'coluna1': row['coluna1'], 'coluna2': row['coluna2'], 'coluna3': row['coluna3']}
            if DATABASE == 'mysql':
                sql = "INSERT INTO tabela (json_data) VALUES (%s)"
                val = (json_data,)
                json_data = json.dumps(document)
                cursor.execute(sql, val)
                cnx.commit()
            elif DATABASE == 'mongodb':
                collection.insert_one(document)
except Exception as err:
    print(f"falha ao inserir na base de dados: {err}") 