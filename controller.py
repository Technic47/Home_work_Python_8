import sqlite3
import messages
import UI
import sys
import os
import database as db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog


def buttons():
    """behavior of UI buttons"""
    db_dir()
    open_db()
    ui.btn_add.clicked.connect(lambda: add())
    ui.btn_new.clicked.connect(lambda: new())
    ui.btn_delete.clicked.connect(lambda: delete())
    ui.btn_search.clicked.connect(lambda: search())
    # ui.btn_merge.clicked.connect(lambda: merge())
    ui.select_db.clicked.connect(lambda: select())
    ui.btn_new_column.clicked.connect(lambda: form_request())


def new():
    """creation of a new DB via two dialogs"""
    global request_param
    request_full = ''
    name = ui.new_name.text()
    if name != '':
        request_full += '(' + request_param + ')'
        request_full = request_full.replace(', )', ')')
        ui.input.setText(request_full)
        db.create(name, request_full)
    else:
        messages.error("Empty line!", "Write name of your DB")

    # name, ok = QInputDialog.getText(ui.input, 'Input Dialog',
    #                                 'Enter db name:')
    # if ok and name != '':
    #     db_name = str(name)
    #
    #     cols, ok = QInputDialog.getText(ui.input, 'Set columns',
    #                                     'Enter columns names:\ncol1 params,col2 params...')
    #     if ok and cols != '':
    #         db_cols = str(cols)
    #         db.create(db_name, db_cols)
    #         item = db_name + '.db'
    #         ui.db_list.addItem(item)


def form_request():
    global request_param
    string = ''
    match ui.new_column.text():
        case '':
            messages.error("Empty line!", "Name your column!")
        case _:
            string += ui.new_column.text() + ' '
            if ui.primary_key.isChecked():
                ui.not_null.setChecked(True)
                string += ui.data_type.itemText(1) + ' '
                string += ui.primary_key.text() + ' '
            else:
                string += ui.data_type.currentText() + ' '
            if ui.not_null.isChecked():
                string += ui.not_null.text() + ' '
            string += ','
            string = string.replace(' ,', ', ')
            request_param += string
            ui.input.setText(request_param)
            ui.new_column.clear()
            ui.primary_key.setChecked(False)
            ui.not_null.setChecked(False)
            print(string)


def open_db():
    """opens current db in tablewidget"""
    name = db.show_current()
    current_db = db.data_path + '/' + name + '.db'
    dbase = sqlite3.connect(current_db)
    cur = dbase.cursor()
    cur.execute(f"SELECT COUNT(2) FROM {name}")
    cols_number = cur.fetchall()
    rows = cols_number[0][0]
    query = f"SELECT * FROM {name}"
    fill = cur.execute(query)
    table_draw(rows, fill)


def add():
    """adds record to current db"""
    data = ui.input.text()
    if data == '':
        messages.error("Empty line!", "Write data in message box.")
    else:
        db.add(data)
        ui.input.setText('')
        open_db()


def delete():
    """deletes in current db inputted data"""
    data = ui.input.text()
    if data == '':
        messages.error("Empty line!", "Write rows numbers in message box.")
    else:
        data_raw = data.replace(';', ',').replace('.', ',').replace(',', ',').replace(' ', ',')
        data = data_raw.replace(',,', ',').split(',')
        print(data)
        db.delete(data[0], data[1])
        ui.input.setText('')
        open_db()


def search():
    """search data in current db"""
    data = ui.input.text()
    if data == '':
        messages.error("Empty line!", "Write your request in message box.")
    else:
        results = (db.search(data))
        ui.input.setText('')

        rows = len(results)
        fill = results
        table_draw(rows, fill)


# def merge(): # do not work yet
#     data = ui.input.text()
#     if data == '':
#         messages.error("Empty line!", "Write your request in message box.")
#     else:
#         path = ui.input.setText('')
#         select = ui.merge_select
#         match select.currentIndex():
#             case 0:
#                 data = select.currentText()
#             case 1:
#                 data = select.currentText()
#             case 2:
#                 data = select.currentText()
#             case 3:
#                 data = select.currentText()
#             case 4:
#                 data = select.currentText()
#             case 5:
#                 data = select.currentText()
#             case 6:
#                 data = select.currentText()
#         db.merge(path, data)


def db_dir():
    """scan dbs and add it to combobox"""
    dirname = 'databases'
    for filename in os.listdir(dirname):
        ui.db_list.addItem(filename)


def select():
    """set selected db in combobox as current"""
    new_db = ui.db_list.currentText().split('.')
    db.set_current(new_db[0])
    open_db()


def table_draw(rows_count, fill):
    """ui tablewidget filling function"""
    name = db.show_current()
    current_db = db.data_path + '/' + name + '.db'
    dbase = sqlite3.connect(current_db)
    cursor = dbase.cursor()

    cursor.execute(f'PRAGMA table_info({name})')
    column_names = [i[1] for i in cursor.fetchall()]
    ui.table.setColumnCount(len(column_names))
    for i in range(len(column_names)):
        ui.table.setColumnWidth(i, 75)
    ui.table.setHorizontalHeaderLabels(column_names)

    ui.table.setRowCount(rows_count)

    tablerow = 0
    for row in fill:
        for i in range(len(column_names)):
            ui.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
        tablerow += 1

    ui.table.setSortingEnabled(1)


request_param = ''

app = UI.QtWidgets.QApplication(sys.argv)
MainWindow = UI.QtWidgets.QMainWindow()
ui = UI.Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
buttons()
sys.exit(app.exec_())
