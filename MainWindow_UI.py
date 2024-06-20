
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
import Directory_Management

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 150, 291, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 150, 75, 21))
        self.pushButton.setObjectName("pushButton")
        self.organize = QtWidgets.QPushButton(Dialog)
        self.organize.setGeometry(QtCore.QRect(120, 230, 75, 23))
        self.organize.setObjectName("organize")
        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(210, 230, 75, 23))
        self.clear.setObjectName("clear")
        self.pushButton.clicked.connect(self.filebrowser)
        self.clear.clicked.connect(self.clearSelectedPath)
        self.organize.clicked.connect(self.OrganizeFiles)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Directory Manager"))
        self.label.setText(_translate("Dialog", "Directory Manager"))
        self.label_2.setText(_translate("Dialog", "Choose a Directory to Organize:"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.organize.setText(_translate("Dialog", "Organize"))
        self.clear.setText(_translate("Dialog", "Clear"))

    def filebrowser(self):
        directory = QFileDialog.getExistingDirectory(Dialog, 'Select a directory')
        if directory:
            self.lineEdit.setText(directory)
    
    def clearSelectedPath(self):
        self.lineEdit.clear()

    def OrganizeFiles(self):
        directory_path = self.lineEdit.text()
        print(f"Selected Directory: {directory_path}")
        if directory_path:
            Directory_Management.run(directory_path)
        else:
            print("Invalid Error {directory_path}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
