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
    ui.btn_open.clicked.connect(lambda: open_db())
    ui.btn_add.clicked.connect(lambda: add())
    ui.btn_new.clicked.connect(lambda: new())
    ui.btn_delete.clicked.connect(lambda: delete())
    ui.btn_search.clicked.connect(lambda: search())
    # ui.btn_merge.clicked.connect(lambda: merge())
    ui.select_db.clicked.connect(lambda: select())
    db_dir()


def new():
    """creation of a new DB via two dialogs"""
    name = ui.new_name.text()
    if name != '':

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


def open_db():
    """opens current db in tablewidget"""
    name = db.show_current()
    current_db = db.data_path + '/' + name + '.db'
    dbase = sqlite3.connect(current_db)
    cur = dbase.cursor()
    cur.execute(f"SELECT COUNT(1) FROM {name}")
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


def delete():
    """deletes in current db inputted data"""
    data = ui.input.text()
    if data == '':
        messages.error("Empty line!", "Write rows numbers in message box.")
    else:
        db.delete(data)
        ui.input.setText('')


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


def table_draw(rows_count, fill):
    """ui tablewidget filling function"""
    name = db.show_current()
    current_db = db.data_path + '/' + name + '.db'
    dbase = sqlite3.connect(current_db)
    cur = dbase.cursor()

    cur.execute(f'PRAGMA table_info({name})')
    column_names = [i[1] for i in cur.fetchall()]
    ui.table.setColumnCount(len(column_names))
    for i in range(len(column_names)):
        ui.table.setColumnWidth(i, 75)
    ui.table.setHorizontalHeaderLabels(column_names)

    ui.table.setRowCount(rows_count)

    tablerow = 0
    for row in fill:
        for i in range(len(column_names)):
            ui.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(row[i]))
        tablerow += 1

    ui.table.setSortingEnabled(1)


app = UI.QtWidgets.QApplication(sys.argv)
MainWindow = UI.QtWidgets.QMainWindow()
ui = UI.Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
buttons()
sys.exit(app.exec_())
