# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 181, 131))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.asLE = QtWidgets.QLineEdit(self.groupBox)
        self.asLE.setObjectName("asLE")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.asLE)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cdLE = QtWidgets.QLineEdit(self.groupBox)
        self.cdLE.setObjectName("cdLE")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cdLE)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pbLE = QtWidgets.QLineEdit(self.groupBox)
        self.pbLE.setObjectName("pbLE")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pbLE)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.hgLE = QtWidgets.QLineEdit(self.groupBox)
        self.hgLE.setObjectName("hgLE")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hgLE)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 110, 159, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.asL = QtWidgets.QLabel(self.groupBox_2)
        self.asL.setObjectName("asL")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.asL)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.cdL = QtWidgets.QLabel(self.groupBox_2)
        self.cdL.setObjectName("cdL")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cdL)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.pbL = QtWidgets.QLabel(self.groupBox_2)
        self.pbL.setObjectName("pbL")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pbL)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.hgL = QtWidgets.QLabel(self.groupBox_2)
        self.hgL.setObjectName("hgL")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hgL)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 70, 62, 20))
        self.label_6.setObjectName("label_6")
        self.servingLE = QtWidgets.QLineEdit(Dialog)
        self.servingLE.setGeometry(QtCore.QRect(110, 70, 108, 20))
        self.servingLE.setObjectName("servingLE")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 30, 198, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.fromCombo = QtWidgets.QComboBox(self.widget)
        self.fromCombo.setObjectName("fromCombo")
        self.fromCombo.addItem("")
        self.horizontalLayout.addWidget(self.fromCombo)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.toCombo = QtWidgets.QComboBox(self.widget)
        self.toCombo.setObjectName("toCombo")
        self.toCombo.addItem("")
        self.horizontalLayout.addWidget(self.toCombo)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fromCombo, self.toCombo)
        Dialog.setTabOrder(self.toCombo, self.servingLE)
        Dialog.setTabOrder(self.servingLE, self.asLE)
        Dialog.setTabOrder(self.asLE, self.cdLE)
        Dialog.setTabOrder(self.cdLE, self.pbLE)
        Dialog.setTabOrder(self.pbLE, self.hgLE)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Given"))
        self.label_2.setText(_translate("Dialog", "Arsenic:"))
        self.label_3.setText(_translate("Dialog", "Cadmium:"))
        self.label_4.setText(_translate("Dialog", "Lead:"))
        self.label_5.setText(_translate("Dialog", "Mercury:"))
        self.groupBox_2.setTitle(_translate("Dialog", "Calculate"))
        self.label_8.setText(_translate("Dialog", "Arsenic:"))
        self.asL.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "Cadmium:"))
        self.cdL.setText(_translate("Dialog", "TextLabel"))
        self.label_10.setText(_translate("Dialog", "Lead:"))
        self.pbL.setText(_translate("Dialog", "TextLabel"))
        self.label_11.setText(_translate("Dialog", "Mercury:"))
        self.hgL.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "Serving Size:"))
        self.label_16.setText(_translate("Dialog", "Convert"))
        self.fromCombo.setItemText(0, _translate("Dialog", "ppm"))
        self.label_17.setText(_translate("Dialog", " to "))
        self.toCombo.setItemText(0, _translate("Dialog", "ug/serving"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
