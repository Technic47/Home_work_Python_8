import UI
import sys

print('controller started')


def functions():
    ui.btn_open.clicked.connect(lambda: open_db())
    ui.btn_add.clicked.connect(lambda: add())


def open_db():
    print('open')
    with open('setup.txt', 'r') as text:
        reader = text.read()
        ui.textBrowser.setText(
            reader
        )


def add():
    with open('setup.txt', 'a') as text:
        data = ui.input.text()
        writer = text.write(data)


app = UI.QtWidgets.QApplication(sys.argv)
MainWindow = UI.QtWidgets.QMainWindow()
ui = UI.Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
functions()
sys.exit(app.exec_())
