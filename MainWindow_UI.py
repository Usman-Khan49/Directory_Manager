from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QFileSystemModel
from PyQt5.QtCore import QDir
import Directory_Management

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 372)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 331, 71))
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
        self.label_2.setGeometry(QtCore.QRect(30, 110, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 130, 401, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.browse = QtWidgets.QPushButton(Dialog)
        self.browse.setGeometry(QtCore.QRect(430, 130, 75, 21))
        self.browse.setObjectName("browse")
        self.organize = QtWidgets.QPushButton(Dialog)
        self.organize.setGeometry(QtCore.QRect(190, 340, 75, 23))
        self.organize.setObjectName("organize")
        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(270, 340, 75, 23))
        self.clear.setObjectName("clear")
        self.Unorganized_DIR = QtWidgets.QTreeView(Dialog)
        self.Unorganized_DIR.setGeometry(QtCore.QRect(20, 160, 321, 171))
        self.Unorganized_DIR.setObjectName("Unorganized_DIR")
        self.browse.clicked.connect(self.filebrowser)
        self.clear.clicked.connect(self.clearSelectedPath)
        self.organize.clicked.connect(self.OrganizeFiles)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Directory Manager"))
        self.label.setText(_translate("Dialog", "Directory Manager"))
        self.label_2.setText(_translate("Dialog", "Choose a Directory to Organize:"))
        self.browse.setText(_translate("Dialog", "Browse"))
        self.organize.setText(_translate("Dialog", "Organize"))
        self.clear.setText(_translate("Dialog", "Clear"))

    def filebrowser(self):
        directory = QFileDialog.getExistingDirectory(None, 'Select a directory')
        if directory:
            self.lineEdit.setText(directory)
            self.model = QFileSystemModel()
            self.model.setRootPath(QDir.rootPath())
            tree = self.Unorganized_DIR
            tree.setModel(self.model)
            tree.setRootIndex(self.model.index(directory))

    def clearSelectedPath(self):
        self.lineEdit.clear()
        self.model.beginResetModel()
        self.model.setRootPath("")
        self.Unorganized_DIR.setRootIndex(QtCore.QModelIndex())
        self.model.endResetModel()

    def OrganizeFiles(self):
        directory_path = self.lineEdit.text()
        print(f"Selected Directory: {directory_path}")
        if directory_path:
            Directory_Management.run(directory_path)
            msg = QMessageBox()
            msg.setWindowTitle('Successful')
            msg.setText('Directory was Organized')
            x = msg.exec_()

            # Update Organized_DIR with the new structure
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Invalid Error')
            msg.setText('Directory was not Specified')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
