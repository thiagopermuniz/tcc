import mysql.connector

cnx = mysql.connector.connect(user='usuario',
                              host='localhost',
                              database='base-tcc')

cursor = cnx.cursor()

with open('script-mysql.sql', 'r') as f:
    script = f.read()

for result in cursor.execute(script, multi=True):
    if result.with_rows:
        print(result.fetchall())

cnx.commit()
cursor.close()
cnx.close()