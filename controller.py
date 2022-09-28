import sqlite3

import UI
import sys
import database as db
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit
# from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel


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
    ui.table.setColumnCount(3)
    ui.table.setColumnWidth(0, 150)
    ui.table.setColumnWidth(1, 150)
    ui.table.setColumnWidth(2, 150)
    ui.table.setHorizontalHeaderLabels(["Col1", "Col2", "Col3"])
    print('1')
    current_db = db.show_current()
    dbase = sqlite3.connect(current_db)
    cur = dbase.cursor()
    print(current_db)
    query = "SELECT * FROM db_1"

    tablerow = 0
    print('query')
    for row in cur.execute(query):
        ui.table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
        ui.table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
        ui.table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
        tablerow += 1
    # dbase = QSqlDatabase.addDatabase(current_db)
    # print(current_db)
    # dbase.setDatabaseName('Your DB')
    # dbase.open()
    # print('DB opened')
    #
    # model = QSqlTableModel()
    # model.setTable("Table")
    # model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    # model.select()
    # ui.tableWidget.setModel(model)


def add():
    pass
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
