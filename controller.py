import sqlite3
import json
import messages
import UI
import sys
import os
import database as db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QFileDialog


def buttons():
    """behavior of UI buttons"""
    db_dir()
    # open_db()
    ui.btn_add.clicked.connect(lambda: add())
    ui.btn_new.clicked.connect(lambda: new())
    ui.btn_delete.clicked.connect(lambda: delete())
    ui.btn_select.clicked.connect(lambda: select())
    ui.btn_merge.clicked.connect(lambda: merge())
    ui.select_db.clicked.connect(lambda: select_db())
    ui.btn_new_column.clicked.connect(lambda: form_request_new())
    ui.btn_import_json.clicked.connect(lambda: import_json())
    ui.btn_export_json.clicked.connect(lambda: export_json())


def new():
    """creation of a new DB via new_db tab"""
    global request_param
    request_full = ''
    name = ui.new_name.text()
    if name != '':
        request_full += '(' + request_param + ')'
        request_full = request_full.replace(', )', ')')
        ui.input.setText(request_full)
        db.create(name, request_full)
        request_param = ''
    else:
        messages.error("Empty line!", "Write name of your DB")


def form_request_new():
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


def form_request_add_col():
    global request_param
    string = ''
    if ui.primary_key_column.isChecked():
        ui.not_null_column.setChecked(True)
        string += ui.data_type_column.itemText(1) + ' '
        string += ui.primary_key_column.text() + ' '
    else:
        string += ui.data_type_column.currentText() + ' '
    if ui.not_null_column.isChecked():
        string += ui.not_null_column.text()
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
    """adds record/column to current db"""
    global request_param
    data = ui.new_name_2.text()
    match data:
        case '':
            messages.error("Empty line!", "Type your request!")
        case _:
            if ui.ad_line.isChecked():
                db.add_line(data)
                ui.input.setText('')
                open_db()

            if ui.add_column.isChecked():
                name = ui.new_name_2.text()
                if name != '':
                    form_request_add_col()
                    print(data, request_param)
                else:
                    messages.error("Empty line!", "Write name of your DB")
                db.add_column(data, request_param)
                ui.input.setText('')
            request_param = ''


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


def select():
    """search data in current db"""
    data = ui.select_column.text()
    if data == '':
        messages.error("Empty line!", "Write name of the column!")
    else:
        if ui.select_request.text() == '':
            messages.error("Empty line!", "Write your request!")
        else:
            request = ui.select_request.text()
            results = (db.select(data, request))

            rows = len(results)
            fill = results
            table_draw(rows, fill)


def merge():
    """merge data from current db and second one"""
    data = ui.current_cols.text()
    data2 = ui.second_cols.text()
    db_get = ui.db_list_2.currentText().split('.')
    db_2 = db_get[0]
    print(data, data2, db_2)
    if data == '' or data2 == '':
        messages.error("Empty line!", "Write col names in message box.")
    else:
        db.merge(data, data2, db_2)

        # rows = len(results)
        # fill = results
        # table_draw(rows, fill)

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
        ui.db_list_2.addItem(filename)


def select_db():
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


def import_json():
    """import json file create new DB and adds data to it"""
    file = QFileDialog.getOpenFileName(None, 'Open file', '', 'json files (*.json);;ALL Files(*)')
    file = file[0].split('/')
    path = file[-1]
    name = path.split('.')
    name = name[0]
    with open(path, 'r', encoding='utf-8') as json_file:
        records = json.load(json_file)

    headers = ''
    for item in records[:1]:
        headers = ', '.join(item)
    headers = '(' + headers + ')'
    if db.create(name, headers):
        for item in records:
            data = ', '.join(item.values())
            db.add_line(data)


def export_json():  # бессовестно скопированно с чьего-то гита, каюсь, устал
    """exports current DB to json"""
    name = db.show_current()
    current_db = db.data_path + '/' + name + '.db'
    db.export_json(current_db)


request_param = ''

app = UI.QtWidgets.QApplication(sys.argv)
MainWindow = UI.QtWidgets.QMainWindow()
ui = UI.Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
buttons()
sys.exit(app.exec_())
