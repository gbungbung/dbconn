#!/usr/bin/python3

import sqlite3
from sqlite3 import Error

#Database file in a specific root folder.
database = r"D:\Code\Projs\Others\dbconn\pydb.db"

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

if __name__ == "__main__":

    #Sql for testing purpose you change whichever you want.
    #TODO: Separate the sql to other file
    sql_create_projects_table=  """CREATE TABLE IF NOT EXISTS projects
                            (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                begin_date text,
                                end_date text
                            );"""

    sql_create_tasks_table= """CREATE TABLE IF NOT EXISTS tasks
                                (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    project_id integer NOT NULL,
                                    start_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects(id)
                                );
                            """

    #Connecting database and make sure connected, then create tables.
    conn= create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
    else:
        print('Database not connected!')
