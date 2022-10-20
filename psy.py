import psycopg2

Class Client:
def __init__(self, first_name, last_name, email, phones=None):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phones = phones

def create_db(conn):
    pass

def add_client(conn, newClient, self=None):
    return Client(self, newClient)

def add_phone(conn, newphone, self=None):
    return Client(self.phones + newphone.phones)

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None, new_client=None, self=None):
    self.client = new_client

def delete_phone(conn, client_id, phone):
    return Client

def delete_client(conn, client_id):
    return Client

def find_client(conn, first_name=None, last_name=None, email=None, phone=None, client_id=None):
    return client_id


with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    conn.rollback()

conn.close()

