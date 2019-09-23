import psycopg2
connection = psycopg2.connect(dbname='sngre123', host='localhost',
   user='postgres', password='postgres', port="5432")
cursor = connection.cursor()
connection.autocommit = True
cursor.execute('CREATE EXTENSION postgis')
connection.close()
