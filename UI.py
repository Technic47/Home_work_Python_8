# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 479)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(420, 0, 231, 271))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_open = QtWidgets.QPushButton(self.groupBox)
        self.btn_open.setGeometry(QtCore.QRect(10, 10, 71, 23))
        self.btn_open.setObjectName("btn_open")
        self.btn_add = QtWidgets.QPushButton(self.groupBox)
        self.btn_add.setGeometry(QtCore.QRect(80, 10, 71, 23))
        self.btn_add.setObjectName("btn_add")
        self.btn_search = QtWidgets.QPushButton(self.groupBox)
        self.btn_search.setGeometry(QtCore.QRect(150, 40, 71, 23))
        self.btn_search.setObjectName("btn_search")
        self.btn_delete = QtWidgets.QPushButton(self.groupBox)
        self.btn_delete.setGeometry(QtCore.QRect(10, 40, 71, 23))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_sort = QtWidgets.QPushButton(self.groupBox)
        self.btn_sort.setGeometry(QtCore.QRect(80, 40, 71, 23))
        self.btn_sort.setObjectName("btn_sort")
        self.btn_new = QtWidgets.QPushButton(self.groupBox)
        self.btn_new.setGeometry(QtCore.QRect(150, 10, 71, 23))
        self.btn_new.setObjectName("btn_new")
        self.btn_export_csv = QtWidgets.QPushButton(self.groupBox)
        self.btn_export_csv.setGeometry(QtCore.QRect(10, 70, 71, 23))
        self.btn_export_csv.setObjectName("btn_export_csv")
        self.btn_import_csv_2 = QtWidgets.QPushButton(self.groupBox)
        self.btn_import_csv_2.setGeometry(QtCore.QRect(80, 70, 71, 23))
        self.btn_import_csv_2.setObjectName("btn_import_csv_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 70, 71, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.input = QtWidgets.QLineEdit(Dialog)
        self.input.setGeometry(QtCore.QRect(10, 10, 401, 51))
        self.input.setObjectName("input")
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setGeometry(QtCore.QRect(10, 80, 401, 391))
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.setObjectName("table")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_open.setText(_translate("Dialog", "Open"))
        self.btn_add.setText(_translate("Dialog", "Add"))
        self.btn_search.setText(_translate("Dialog", "Search"))
        self.btn_delete.setText(_translate("Dialog", "Delete"))
        self.btn_sort.setText(_translate("Dialog", "Sort"))
        self.btn_new.setText(_translate("Dialog", "New"))
        self.btn_export_csv.setText(_translate("Dialog", "Export csv"))
        self.btn_import_csv_2.setText(_translate("Dialog", "Import csv"))
        self.pushButton_9.setText(_translate("Dialog", "PushButton"))
