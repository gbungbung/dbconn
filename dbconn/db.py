import sqlite3
from sqlite3 import Error
import sqls

def create_connection(db):
    """create a database connection
    :param db file: database file
    :return: connection object or None
    """
    connection= None
    try:
        connection= sqlite3.connect(db)
        return connection
    except Error as e:
        print(e)
    return connection

def create_table(connection, create_sql):
    """Create table from create_table_sql statement
    :param connection, create_table_sql:
    """
    try:
        c= connection.cursor()
        c.execute(create_sql)
    except Error as e:
        print(e)

def create(connection, create_db):
    """Create database from create_db param with sql code
    :param connection, create_db:
    """
    database = r"D:\Code\Projs\Others\dbconn>pydb.db"
    connected= create_connection(database)
    if connected is not None:
        create_table(connection, create_db)
    else:
        print('Something went wrong!')