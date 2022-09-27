import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create(self):
        try:
            sqlite_connection = sqlite3.connect(self.path)
            sqlite_create_table_query = '''CREATE TABLE new (
                                        name TEXT NOT NULL,
                                        age INTEGER NOT NULL UNIQUE,
                                        phone INTEGER NOT NULL);'''

            cursor = sqlite_connection.cursor()
            print("База данных подключена к SQLite")
            cursor.execute(sqlite_create_table_query)
            sqlite_connection.commit()
            print("Таблица SQLite создана")

            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (sqlite_connection):
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    def test_connect(self):
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

    def show_path(self):
        try:
            sqlite_connection = sqlite3.connect('sqlite_python.db')
            cursor = sqlite_connection.cursor()

            print(self.path)
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (sqlite_connection):
                sqlite_connection.close()

    def open(self):
        try:
            sqlite_connection = sqlite3.connect('sqlite_python.db')
            cursor = sqlite_connection.cursor()
            print("База данных создана и успешно подключена к SQLite")

            with open('sqlite_create_tables.sql', 'r') as sqlite_file:
                sql_script = sqlite_file.read()
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (sqlite_connection):
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

        cursor.executescript(sql_script)
        print("Скрипт SQLite успешно выполнен")

    def add(self, data):
        try:
            sqlite_connection = sqlite3.connect(self.path)
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

    def show(self):
        try:
            sqlite_connection = sqlite3.connect(self.path)
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

# db = Database('databases/new.db')
# db.show_path()
# db.test_connect()
# db.create()
# db.add("'Pavel', 32, 2354234")
# db.add("'Andrey', 55, 24265")
# db.add("'Svetlana', 50, 8798754")
# db.show()
