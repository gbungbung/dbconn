#Sql for testing purpose you change whichever you want
sql_create_projects_table=  """CREATE TABLE IF NOT EXISTS projects
                            (
                                id integer PRIMARY NUMBER,
                                name text NOT NULL,
                                begin_date text,
                                end_date text,
                            );"""

from dbconn.db import create

def mydb(connection, sql_create_projects_table):
    return create(connection, sql_create_projects_table)