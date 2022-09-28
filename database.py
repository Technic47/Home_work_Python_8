import sqlite3


# def connect(func):
#     def wrapper():
#         name = show_current()
#         current_db = data_path + '/' + name + '.db'
#         try:
#             sqlite_connection = sqlite3.connect(current_db)
#             cursor = sqlite_connection.cursor()
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


def create(name, data):
    """forming CREATE sql task"""
    path = data_path + '/' + name + '.db'
    try:
        sqlite_connection = sqlite3.connect(path)
        cols_raw = data.replace(';', ',').replace('.', ',').replace(',', ',').replace(' ', ',')
        cols_raw = cols_raw.replace(',,', ',')
        cols = cols_raw.replace(',', ', ')
        sqlite_create_table_query = f'''CREATE TABLE {name} ({cols})'''

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


def set_current(data) -> None:
    """change current db to data in setup file"""
    with open(setup, 'w') as file:
        file.write(data)


def show_current() -> str:
    """shows current db from setup file"""
    with open(setup, 'r') as file:
        current_database = file.read()
    return current_database


def add(data):
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

        insert = f'''INSERT INTO {name} VALUES ({data})'''
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


def delete(data):
    """forming DELETE sql task"""
    name = show_current()
    current_db = data_path + '/' + name + '.db'
    try:
        sqlite_connection = sqlite3.connect(current_db)
        print(data)

        sql_delete = f'''DELETE FROM {name} WHERE text1 = ?'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sql_delete, (data,))
        sqlite_connection.commit()
        print("Deleted")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def search(data):
    """forming SELECT sql task"""
    name = show_current()
    current_db = data_path + '/' + name + '.db'
    try:
        sqlite_connection = sqlite3.connect(current_db)
        sql_delete = f'''SELECT * FROM {name} WHERE text1 = ?'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sql_delete, (data,))
        record = cursor.fetchall()
        print("Selected")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    return record


# def merge(path, method): # do not work yet
#     name = show_current()
#     current_db = data_path + '/' + name + '.db'
#     try:
#         sqlite_connection = sqlite3.connect(current_db)
#         sql_delete = f'''SELECT * FROM {name} WHERE text1 = ?'''
#         cursor = sqlite_connection.cursor()
#         cursor.execute(sql_delete, (data,))
#         record = cursor.fetchall()
#         print("Selected")
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Ошибка при подключении к sqlite", error)
#     finally:
#         if (sqlite_connection):
#             sqlite_connection.close()


# def sql_constructor(action, data): # stupid idea
#     name = show_current()
#     current_db = data_path + '/' + name + '.db'
#     try:
#         sqlite_connection = sqlite3.connect(current_db)
#         match action:
#             case 'create':
#                 sql_action = 'CREATE TABLE'
#             case 'insert':
#                 sql_action = 'INSERT INTO'
#                 addition = 'VALUES'
#             case 'delete':
#                 sql_action = 'DELETE FROM'
#                 addition = 'WHERE'
#
#
#         sql_request = f'''{sql_action} {name} {addition} text1 = ?'''
#         cursor = sqlite_connection.cursor()
#         cursor.execute(sql_request)
#         sqlite_connection.commit()
#         print("Deleted")
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Ошибка при подключении к sqlite", error)
#     finally:
#         if (sqlite_connection):
#             sqlite_connection.close()


data_path = r'databases'
setup = 'setup.txt'
