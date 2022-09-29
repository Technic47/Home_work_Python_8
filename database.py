import sqlite3


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


def create(name, data):
    """forming CREATE sql task"""
    path = data_path + '/' + name + '.db'
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


# def merge(data, data2, db_2): # не работает(((
#     name = show_current()
#     current_db = data_path + '/' + name + '.db'
#     second_db = data_path + '/' + db_2 + '.db'
#     sqlite_connection = False
#     try:
#         sqlite_connection = sqlite3.connect(current_db)
#
#         print('join prepare')
#         sql_join = f'''SELECT {data} FROM {name} UNION SELECT {data2} FROM {db_2}'''
#         print(sql_join)
#         cursor = sqlite_connection.cursor()
#         cursor.execute(sql_join)
#         record = cursor.fetchall()
#         print("Joined")
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Ошибка при подключении к sqlite", error)
#     finally:
#         if (sqlite_connection):
#             sqlite_connection.close()
#     return record


data_path = r'databases'
setup = 'setup.txt'
