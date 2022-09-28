import sqlite3


def create(name, data):
    path = data_path + '/' + name + '.db'
    try:
        sqlite_connection = sqlite3.connect(path)
        cols_row = data.replace(';', ',').replace('.', ',').replace(',', ',').replace(' ', ',')
        cols_row = cols_row.replace(',,', ',')
        cols = cols_row.replace(',', ', ')
        sqlite_create_table_query = f'''CREATE TABLE new ({cols})'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")
        set_current(path)
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


def test_connect():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def show_path(path):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()

        print(path)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def open_current():
    try:
        current_db = show_current()
        sqlite_connection = sqlite3.connect(current_db)
        cursor = sqlite_connection.cursor()
        sqlite_select_query = """SELECT * from {current_db}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

    cursor.executescript(sql_script)
    print("Скрипт SQLite успешно выполнен")


def add(data, path):
    try:
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        insert = f"""INSERT INTO new VALUES ({data})"""
        cursor.execute(insert)
        sqlite_connection.commit()
        print("Added")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def show(path):
    try:
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()

        select = "SELECT rowid, * FROM new"
        cursor.execute(select)
        items = cursor.fetchall()
        for i in items:
            print(i)

        # print(cursor.fetchall())
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


data_path = r'databases'
setup = 'setup.txt'
