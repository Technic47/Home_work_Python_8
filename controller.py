import UI
import sys
import database as db
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit


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


def open_db()


def add():
    data = ui.input.text()
    if data == '':
        ui.textBrowser.setText('Print name of a new database above!')
    else:
        db.add(data)
        ui.input.setText('')
        ui.textBrowser.setText('')


app = UI.QtWidgets.QApplication(sys.argv)
MainWindow = UI.QtWidgets.QMainWindow()
ui = UI.Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
buttons()
sys.exit(app.exec_())
