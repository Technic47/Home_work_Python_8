import UI
import sys
import database as db


def functions():
    # ui.btn_open.clicked.connect(lambda: open_db())
    ui.btn_add.clicked.connect(lambda: add())
    ui.btn_new.clicked.connect(lambda: new())


def new():
    folder = 'databases/'
    name = ui.input.text()
    if name == '':
        ui.textBrowser.setText('Print name of a new database above!')
    else:
        path = folder + name + '.db'
        new_db = db.Database(path)
        new_db.create()
        ui.input.setText('')
    return


# def add():
#     current().


app = UI.QtWidgets.QApplication(sys.argv)
MainWindow = UI.QtWidgets.QMainWindow()
ui = UI.Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
functions()
sys.exit(app.exec_())
