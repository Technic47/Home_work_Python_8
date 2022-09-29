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
        Dialog.resize(659, 469)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(420, 0, 231, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_delete = QtWidgets.QPushButton(self.groupBox)
        self.btn_delete.setGeometry(QtCore.QRect(10, 40, 71, 23))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_import_json = QtWidgets.QPushButton(self.groupBox)
        self.btn_import_json.setGeometry(QtCore.QRect(10, 70, 71, 23))
        self.btn_import_json.setObjectName("btn_import_json")
        self.select_db = QtWidgets.QPushButton(self.groupBox)
        self.select_db.setGeometry(QtCore.QRect(10, 10, 71, 23))
        self.select_db.setObjectName("select_db")
        self.db_list = QtWidgets.QComboBox(self.groupBox)
        self.db_list.setGeometry(QtCore.QRect(81, 11, 139, 21))
        self.db_list.setEditable(False)
        self.db_list.setObjectName("db_list")
        self.btn_export_json = QtWidgets.QPushButton(self.groupBox)
        self.btn_export_json.setGeometry(QtCore.QRect(80, 70, 71, 23))
        self.btn_export_json.setObjectName("btn_export_json")
        self.input = QtWidgets.QLineEdit(Dialog)
        self.input.setGeometry(QtCore.QRect(10, 10, 401, 31))
        self.input.setObjectName("input")
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setGeometry(QtCore.QRect(10, 50, 401, 411))
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.setObjectName("table")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(420, 210, 231, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.New_DB = QtWidgets.QWidget()
        self.New_DB.setObjectName("New_DB")
        self.new_column = QtWidgets.QLineEdit(self.New_DB)
        self.new_column.setGeometry(QtCore.QRect(0, 40, 113, 23))
        self.new_column.setObjectName("new_column")
        self.btn_new = QtWidgets.QPushButton(self.New_DB)
        self.btn_new.setGeometry(QtCore.QRect(150, 200, 71, 23))
        self.btn_new.setObjectName("btn_new")
        self.btn_new_column = QtWidgets.QPushButton(self.New_DB)
        self.btn_new_column.setGeometry(QtCore.QRect(150, 40, 71, 23))
        self.btn_new_column.setObjectName("btn_new_column")
        self.new_name = QtWidgets.QLineEdit(self.New_DB)
        self.new_name.setGeometry(QtCore.QRect(0, 10, 113, 23))
        self.new_name.setObjectName("new_name")
        self.primary_key = QtWidgets.QCheckBox(self.New_DB)
        self.primary_key.setGeometry(QtCore.QRect(0, 100, 91, 17))
        self.primary_key.setObjectName("primary_key")
        self.not_null = QtWidgets.QCheckBox(self.New_DB)
        self.not_null.setGeometry(QtCore.QRect(0, 120, 81, 17))
        self.not_null.setObjectName("not_null")
        self.checkBox_3 = QtWidgets.QCheckBox(self.New_DB)
        self.checkBox_3.setGeometry(QtCore.QRect(0, 140, 81, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.data_type = QtWidgets.QComboBox(self.New_DB)
        self.data_type.setGeometry(QtCore.QRect(0, 70, 113, 22))
        self.data_type.setObjectName("data_type")
        self.data_type.addItem("")
        self.data_type.addItem("")
        self.data_type.addItem("")
        self.label = QtWidgets.QLabel(self.New_DB)
        self.label.setGeometry(QtCore.QRect(150, 10, 71, 23))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.New_DB, "")
        self.Add = QtWidgets.QWidget()
        self.Add.setObjectName("Add")
        self.ad_line = QtWidgets.QRadioButton(self.Add)
        self.ad_line.setGeometry(QtCore.QRect(10, 0, 82, 23))
        self.ad_line.setChecked(True)
        self.ad_line.setObjectName("ad_line")
        self.add_column = QtWidgets.QRadioButton(self.Add)
        self.add_column.setGeometry(QtCore.QRect(130, 0, 82, 23))
        self.add_column.setObjectName("add_column")
        self.data_type_column = QtWidgets.QComboBox(self.Add)
        self.data_type_column.setGeometry(QtCore.QRect(0, 70, 113, 22))
        self.data_type_column.setObjectName("data_type_column")
        self.data_type_column.addItem("")
        self.data_type_column.addItem("")
        self.data_type_column.addItem("")
        self.primary_key_column = QtWidgets.QCheckBox(self.Add)
        self.primary_key_column.setGeometry(QtCore.QRect(0, 100, 91, 17))
        self.primary_key_column.setObjectName("primary_key_column")
        self.checkBox_4 = QtWidgets.QCheckBox(self.Add)
        self.checkBox_4.setGeometry(QtCore.QRect(0, 140, 81, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.not_null_column = QtWidgets.QCheckBox(self.Add)
        self.not_null_column.setGeometry(QtCore.QRect(0, 120, 81, 17))
        self.not_null_column.setObjectName("not_null_column")
        self.new_name_2 = QtWidgets.QLineEdit(self.Add)
        self.new_name_2.setGeometry(QtCore.QRect(0, 40, 113, 23))
        self.new_name_2.setObjectName("new_name_2")
        self.label_2 = QtWidgets.QLabel(self.Add)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 71, 23))
        self.label_2.setObjectName("label_2")
        self.btn_add = QtWidgets.QPushButton(self.Add)
        self.btn_add.setGeometry(QtCore.QRect(150, 200, 71, 23))
        self.btn_add.setObjectName("btn_add")
        self.tabWidget.addTab(self.Add, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_merge = QtWidgets.QPushButton(self.tab)
        self.btn_merge.setGeometry(QtCore.QRect(150, 200, 71, 23))
        self.btn_merge.setObjectName("btn_merge")
        self.merge_method = QtWidgets.QComboBox(self.tab)
        self.merge_method.setGeometry(QtCore.QRect(0, 100, 113, 21))
        self.merge_method.setEditable(False)
        self.merge_method.setObjectName("merge_method")
        self.merge_method.addItem("")
        self.merge_method.addItem("")
        self.merge_method.addItem("")
        self.merge_method.addItem("")
        self.merge_method.addItem("")
        self.merge_method.addItem("")
        self.merge_method.addItem("")
        self.merge_method.addItem("")
        self.db_list_2 = QtWidgets.QComboBox(self.tab)
        self.db_list_2.setGeometry(QtCore.QRect(0, 10, 113, 21))
        self.db_list_2.setEditable(False)
        self.db_list_2.setObjectName("db_list_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 71, 23))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 91, 23))
        self.label_4.setObjectName("label_4")
        self.current_cols = QtWidgets.QLineEdit(self.tab)
        self.current_cols.setGeometry(QtCore.QRect(0, 40, 113, 23))
        self.current_cols.setObjectName("current_cols")
        self.second_cols = QtWidgets.QLineEdit(self.tab)
        self.second_cols.setGeometry(QtCore.QRect(0, 70, 113, 23))
        self.second_cols.setObjectName("second_cols")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(120, 40, 91, 23))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(120, 70, 91, 23))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 100, 231, 111))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_select = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_select.setGeometry(QtCore.QRect(150, 70, 71, 23))
        self.btn_select.setObjectName("btn_select")
        self.select_column = QtWidgets.QLineEdit(self.groupBox_2)
        self.select_column.setGeometry(QtCore.QRect(10, 10, 113, 23))
        self.select_column.setText("")
        self.select_column.setObjectName("select_column")
        self.select_request = QtWidgets.QLineEdit(self.groupBox_2)
        self.select_request.setGeometry(QtCore.QRect(10, 40, 113, 23))
        self.select_request.setText("")
        self.select_request.setObjectName("select_request")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(150, 10, 71, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(150, 40, 71, 20))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_delete.setText(_translate("Dialog", "Delete"))
        self.btn_import_json.setText(_translate("Dialog", "Import .json"))
        self.select_db.setText(_translate("Dialog", "Select DB"))
        self.btn_export_json.setText(_translate("Dialog", "Export .json"))
        self.btn_new.setText(_translate("Dialog", "Create"))
        self.btn_new_column.setText(_translate("Dialog", "Add column"))
        self.primary_key.setText(_translate("Dialog", "PRIMARY KEY"))
        self.not_null.setText(_translate("Dialog", "NOT NULL"))
        self.checkBox_3.setText(_translate("Dialog", "OPTION"))
        self.data_type.setItemText(0, _translate("Dialog", "TEXT"))
        self.data_type.setItemText(1, _translate("Dialog", "INT"))
        self.data_type.setItemText(2, _translate("Dialog", "Unique"))
        self.label.setText(_translate("Dialog", "  Table name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.New_DB), _translate("Dialog", "New DB"))
        self.ad_line.setText(_translate("Dialog", "Add line"))
        self.add_column.setText(_translate("Dialog", "Add column"))
        self.data_type_column.setItemText(0, _translate("Dialog", "TEXT"))
        self.data_type_column.setItemText(1, _translate("Dialog", "INT"))
        self.data_type_column.setItemText(2, _translate("Dialog", "Unique"))
        self.primary_key_column.setText(_translate("Dialog", "PRIMARY KEY"))
        self.checkBox_4.setText(_translate("Dialog", "OPTION"))
        self.not_null_column.setText(_translate("Dialog", "NOT NULL"))
        self.label_2.setText(_translate("Dialog", "What to add"))
        self.btn_add.setText(_translate("Dialog", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Add), _translate("Dialog", "Add to current"))
        self.btn_merge.setText(_translate("Dialog", "Merge"))
        self.merge_method.setItemText(0, _translate("Dialog", "UNION"))
        self.merge_method.setItemText(1, _translate("Dialog", "LEFT JOIN"))
        self.merge_method.setItemText(2, _translate("Dialog", "LEFT NULL"))
        self.merge_method.setItemText(3, _translate("Dialog", "RIGHT JOIN"))
        self.merge_method.setItemText(4, _translate("Dialog", "RIGHT NUL"))
        self.merge_method.setItemText(5, _translate("Dialog", "INNER JOIN"))
        self.merge_method.setItemText(6, _translate("Dialog", "FULL JOIN"))
        self.merge_method.setItemText(7, _translate("Dialog", "FULL NULL"))
        self.label_3.setText(_translate("Dialog", "     Method"))
        self.label_4.setText(_translate("Dialog", "Second table name"))
        self.label_5.setText(_translate("Dialog", "Current table cols"))
        self.label_6.setText(_translate("Dialog", "Second table cols"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Merge"))
        self.btn_select.setText(_translate("Dialog", "Select"))
        self.label_7.setText(_translate("Dialog", "Select column"))
        self.label_8.setText(_translate("Dialog", "    Request"))
