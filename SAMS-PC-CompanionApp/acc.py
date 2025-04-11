import psycopg2
import os



def connect_to_db():
    db = os.environ.get('DB')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    try:
        psycopg2.connect(dbname=db, user=db_user, password=db_pass, host=db_host, port=db_port)
        print("connect success")
    except psycopg2.OperationalError:
        print("No Internet")
    
connect_to_db()