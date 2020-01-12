# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pw_generator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.uppercase = QtWidgets.QCheckBox(self.centralwidget)
        self.uppercase.setGeometry(QtCore.QRect(100, 240, 150, 17))
        self.uppercase.setObjectName("uppercase")
        self.specialcharacter = QtWidgets.QCheckBox(self.centralwidget)
        self.specialcharacter.setGeometry(QtCore.QRect(100, 260, 200, 31))
        self.specialcharacter.setObjectName("specialcharacter")
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(320, 440, 91, 31))
        self.generate.setObjectName("generate")
        self.lenght = QtWidgets.QLineEdit(self.centralwidget)
        self.lenght.setGeometry(QtCore.QRect(370, 340, 121, 31))
        self.lenght.setObjectName("lenght")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(70, 330, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLineEdit(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 80, 611, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.generate.clicked.connect(lambda: self.label.setText(self.generatepw()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uppercase.setText(_translate("MainWindow", "UpperCase"))
        self.specialcharacter.setText(_translate("MainWindow", "Special Characters"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.label1.setText(_translate("MainWindow", "How many digits do you want?"))

    def generatepw(self, ):
        from random import sample, randint
        lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        upper = [i.upper() for i in lower]
        special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "{", "}", "[", "]", "|", ";", ":",
                   "'", '"', ",", "<", ".", ">", "/", "?", "`", "~"]
        password = ""
        pw = []

        upper_check = self.uppercase.isChecked()

        special_check = self.specialcharacter.isChecked()

        while len(pw) < int(self.lenght.text()):
            num = randint(1, 3)
            if num == 1:
                if special_check == True:
                    pw.append(sample(special, 1)[0])
            if num == 2:
                if upper_check == True:
                    pw.append(sample(upper, 1)[0])
            if num == 3:
                pw.append(sample(lower, 1)[0])

        for x in pw:
            password = password + str(x)
        return password


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
