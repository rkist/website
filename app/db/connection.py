import psycopg2

def connect_to_db():
    host = 'localhost'
    database = 'website'
    user = 'postgres'
    password = 'postgres'
    return psycopg2.connect(host=host, database=database, user=user, password=password)