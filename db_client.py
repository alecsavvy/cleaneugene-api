#db_client.py

import os
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

RDB_HOST = 'localhost'
RDB_PORT = 28015

# Database is todo and table is notes
PROJECT_DB = 'CleanEugene'
PROJECT_TABLE = 'reports'

# Set up db connection client
db_connection = r.connect(RDB_HOST, RDB_PORT)

# Function is for cross-checking database and table exists
def dbSetup():
    try:
        r.db_create(PROJECT_DB).run(db_connection)
        print("Database Setup Completed.")
    except RqlRuntimeError:
        try:
            r.db(PROJECT_DB).table_create(PROJECT_TABLE).run(db_connection)
            print "Table Creation Completed."
        except:
            print "Table already exists. Nothing to do."

dbSetup()