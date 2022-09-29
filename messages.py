from PyQt5.QtWidgets import QMessageBox


def error(description: str, action: str):
    """pop up error message constructor"""
    error = QMessageBox()
    error.setWindowTitle("Error")
    error.setText(description)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Ok)
    # error.setDefaultButton(QMessageBox.Ok)
    error.setInformativeText(action)
    # error.setDetailedText('Details of error')
    error.exec_()


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