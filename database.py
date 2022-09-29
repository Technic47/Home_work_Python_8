import os.path
import sqlite3
import json

import messages


# def connect(func):
#     def wrapper():
#         name = show_current()
#         current_db = data_path + '/' + name + '.db'
#         sqlite_connection = False
#         try:
#
#             sqlite_connection = sqlite3.connect(current_db)
#             cursor = sqlite_connection.cursor()
#             # func()
#             cursor.execute(func())
#             sqlite_connection.commit()
#             cursor.close()
#
#         except sqlite3.Error as error:
#             print("Ошибка при подключении к sqlite", error)
#         finally:
#             if (sqlite_connection):
#                 sqlite_connection.close()
#
#     return wrapper


def create(name: str, data: str):
    """forming CREATE sql task"""
    path = data_path + '/' + name + '.db'
    if os.path.exists(path):
        messages.error('File already exist!', '')
        return
    else:
        sqlite_connection = False
        try:
            sqlite_connection = sqlite3.connect(path)

            sqlite_create_table_query = f'''CREATE TABLE IF NOT EXISTS {name} {data}'''
            print(sqlite_create_table_query)
            cursor = sqlite_connection.cursor()
            cursor.execute(sqlite_create_table_query)
            sqlite_connection.commit()
            print("Таблица SQLite создана")
            set_current(name)
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (sqlite_connection):
                sqlite_connection.close()
        return True


def set_current(data) -> None:
    """change current db to data in setup file"""
    with open(setup, 'w') as file:
        file.write(data)


def show_current() -> str:
    """shows current db from setup file"""
    with open(setup, 'r') as file:
        current_database = file.read()
    return current_database


def add_line(data):
    """forming INSERT sql task"""
    name = show_current()
    current_db = data_path + '/' + name + '.db'
    try:
        sqlite_connection = sqlite3.connect(current_db)
        data_raw = data.replace(';', ',').replace('.', ',').replace(',', ',').replace(' ', ',')
        data_raw = data_raw.replace(',,', ',').split(',')
        string = ''
        for item in data_raw:
            string += "'" + item + "'"
        data = string.replace("''", "', '")
        print(data)

        insert = f'''INSERT INTO {name} VALUES ({data})'''
        print(insert)
        cursor = sqlite_connection.cursor()
        cursor.execute(insert)
        sqlite_connection.commit()
        print("Added")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def add_column(col, data):
    """forming ALTER sql task"""
    name = show_current()
    current_db = data_path + '/' + name + '.db'
    try:
        sqlite_connection = sqlite3.connect(current_db)

        insert = f'''ALTER TABLE {name} ADD COLUMN {col} {data}'''
        print(insert)
        cursor = sqlite_connection.cursor()
        cursor.execute(insert)
        sqlite_connection.commit()
        print("Added")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def delete(col, data):
    """forming DELETE sql task"""
    name = show_current()
    current_db = data_path + '/' + name + '.db'
    try:
        sqlite_connection = sqlite3.connect(current_db)
        cursor = sqlite_connection.cursor()
        print(col, data)
        sql_delete = f'''DELETE FROM {name} WHERE {col} = ?'''

        cursor.execute(sql_delete, (data,))
        sqlite_connection.commit()
        print("Deleted")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def select(data, request):
    """forming SELECT * sql task"""
    name = show_current()
    current_db = data_path + '/' + name + '.db'
    sqlite_connection = False
    try:
        sqlite_connection = sqlite3.connect(current_db)
        sql_select = f'''SELECT * FROM {name} WHERE {data} = ?'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sql_select, (str(request),))
        record = cursor.fetchall()
        print(record)
        print("Selected")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    return record


def export_json(current_db):
    connection, cursor = openConnection(current_db)
    # select all the tables from the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    # for each of the tables , select all the records from the table
    for table_name in tables:
        # Get the records in table
        results = getAllRecordsInTable(table_name['name'], current_db)

        # generate and save JSON files with the table name for each of the database tables and save in results folder
        with open('./results/' + table_name['name'] + '.json', 'w') as the_file:
            the_file.write(results)
    # close connection
    connection.close()


def getAllRecordsInTable(table_name, pathToSqliteDb):
    conn, curs = openConnection(pathToSqliteDb)
    conn.row_factory = dict_factory
    curs.execute("SELECT * FROM '{}' ".format(table_name))
    # fetchall as result
    results = curs.fetchall()
    # close connection
    conn.close()
    return json.dumps(results)


def openConnection(pathToSqliteDb):
    connection = sqlite3.connect(pathToSqliteDb)
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    return connection, cursor


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def merge(data, data2, db_2):  # не работает(((
    name = show_current()
    current_db = data_path + '/' + name + '.db'
    target = 'target'
    target_db = data_path + '/' + target + '.db'
    sqlite_connection = False
    try:
        sqlite_connection = sqlite3.connect(target_db)

        print('join prepare')
        sql_join = f'''CREATE TABLE {target} AS SELECT {data} FROM {name}
         UNION
          SELECT {data2} FROM {db_2}'''
        print(sql_join)
        cursor = sqlite_connection.cursor()
        cursor.execute(sql_join)
        record = cursor.fetchall()
        print("Joined")
        set_current(target)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    return record


data_path = r'databases'
setup = 'setup.txt'
