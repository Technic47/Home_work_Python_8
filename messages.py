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
