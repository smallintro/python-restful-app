'''
@author: Sushil Prasad
@summary: create db connection and execute sql statements
'''
import os
import sys
import psycopg2
from psycopg2 import Error
from psycopg2._psycopg import cursor

sys.path.insert(1, os.path.abspath(".."))

def _create_connection():
    dbhost, dbport, dbname, username, userpass = "localhost",5432,"postgres","postgres","ABC_abc1"
    # print(dbhost,dbport,dbname,username,userpass)
    connection = ''
    try:
        connection = psycopg2.connect(host=dbhost, port=str(dbport), database=dbname, user=username, password=userpass)
        # print("Connection created\n",connection)
    except(Exception, psycopg2.DatabaseError) as error:
        print("Creating connection failed\n", error)
    return connection


def _get_connection():
    connection = _create_connection()
    return connection


def _execute_db_command(sql_statement):
    print("\nstart executing ", sql_statement, "\n")
    try:
        conn = _get_connection()
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("_execute_db_command failed for sql: ", sql_statement, error)
        
    finally:
        if (conn):
            cursor.close()
            conn.close()


def _execute_select_command(sql_statement):
    print("\nstart executing ", sql_statement, "\n")
    cursor = ''
    try:
        conn = _get_connection()
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("_execute_select_command failed for sql: ", sql_statement, error)
        
    return cursor, conn


def execute_create_sql():
    create_sql = """CREATE TABLE "T_BRAND_INFO" (brand_id NUMERIC NOT NULL, 
    brand_name VARCHAR, PRIMARY KEY (brand_id))"""
    _execute_db_command(create_sql)
    create_sql = '''CREATE TABLE "T_MOBILE_INFO" (mobile_id VARCHAR NOT NULL, 
    mobile_name VARCHAR NOT NULL, brand_id INTEGER, storage_size BIGINT NOT NULL, ram_size INTEGER NOT NULL, 
    added_on TIMESTAMP WITHOUT TIME ZONE NOT NULL, sold_on TIMESTAMP WITHOUT TIME ZONE, PRIMARY KEY (mobile_id), 
    FOREIGN KEY(brand_id) REFERENCES "T_BRAND_INFO" (brand_id));'''
    _execute_db_command(create_sql)


def execute_select_sql(mobile_id):
    select_sql = "select * from T_MOBILE_INFO where mobile_id={};"
    cursor, conn = _execute_select_command(select_sql.format(mobile_id))
    for record in cursor:
        print('mobile_id ', record[0])
        print('mobile_name ', record[1])
        print('brand_id ', record[2])
    if (conn):
        cursor.close()
        conn.close()


if __name__ == "__main__":
    execute_select_sql('o')