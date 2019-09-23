import psycopg2
connection = psycopg2.connect(host='localhost',
    user='postgres',password='postgres', port="5432")
connection.autocommit = True
cursor = connection.cursor()
cursor.execute('CREATE DATABASE sngre123')
