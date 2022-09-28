import sqlite3

import UI
import sys
import database as db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog


def buttons():
    ui.btn_open.clicked.connect(lambda: open_db())
    ui.btn_add.clicked.connect(lambda: add())
    ui.btn_new.clicked.connect(lambda: new())


def new():
    db_name = ''
    db_cols = ''
    name, ok = QInputDialog.getText(ui.input, 'Input Dialog',
                                    'Enter db name:')
    if ok and name != '':
        db_name = str(name)

    cols, ok = QInputDialog.getText(ui.input, 'Set columns',
                                    'Enter columns names:')
    if ok and cols != '':
        db_cols = str(cols)

    db.create(db_name, db_cols)


def open_db():
    name = db.show_current()
    current_db = db.data_path + '/' + name + '.db'
    dbase = sqlite3.connect(current_db)
    cur = dbase.cursor()
    cur.execute(f'PRAGMA table_info({name})')
    column_names = [i[1] for i in cur.fetchall()]
    print(column_names)

    ui.table.setColumnCount(len(column_names))
    for i in range(len(column_names)):
        ui.table.setColumnWidth(i, 75)
    ui.table.setHorizontalHeaderLabels(column_names)

    query = f"SELECT * FROM {name}"

    ui.table.setRowCount(50)

    tablerow = 0

    for row in cur.execute(query):
        for i in range(len(column_names)):
            ui.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(row[i]))
        tablerow += 1


def add():
    data = ui.input.text()
    if data == '':
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setText("Empty line!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.setInformativeText("Write data in message box.")
        error.exec_()
    else:
        db.add(data)
        ui.input.setText('')


app = UI.QtWidgets.QApplication(sys.argv)
MainWindow = UI.QtWidgets.QMainWindow()
ui = UI.Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
buttons()
sys.exit(app.exec_())
