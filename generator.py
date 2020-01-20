#Copyright MaoMaoCake, 2020
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.window = MainWindow #for fuction later
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.uppercase = QtWidgets.QCheckBox(self.centralwidget)
        self.uppercase.setGeometry(QtCore.QRect(100, 230, 150, 40))
        self.uppercase.setObjectName("uppercase")

        self.specialcharacter = QtWidgets.QCheckBox(self.centralwidget)
        self.specialcharacter.setGeometry(QtCore.QRect(100, 260, 200, 40))
        self.specialcharacter.setObjectName("specialcharacter")

        self.number_box = QtWidgets.QCheckBox(self.centralwidget)
        self.number_box.setGeometry(QtCore.QRect(100, 200, 200, 40))
        self.number_box.setObjectName("number_box")

        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(320, 450, 91, 31))
        self.generate.setObjectName("generate")

        self.generate2 = QtWidgets.QPushButton(self.centralwidget)
        self.generate2.setGeometry(QtCore.QRect(500, 450, 140, 31))
        self.generate2.setObjectName("generate2")

        self.lenght = QtWidgets.QLineEdit(self.centralwidget)
        self.lenght.setGeometry(QtCore.QRect(370, 340, 121, 31))
        self.lenght.setObjectName("lenght")

        self.times = QtWidgets.QLineEdit(self.centralwidget)
        self.times.setGeometry(QtCore.QRect(500, 410, 121, 31))
        self.times.setObjectName("times")

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

        self.estimate = QtWidgets.QLabel(self.centralwidget)
        self.estimate.setGeometry(QtCore.QRect(450, 230, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.estimate.setFont(font)
        self.estimate.setObjectName("estimate_time")

        self.time_txt = QtWidgets.QLabel(self.centralwidget)
        self.time_txt.setGeometry(QtCore.QRect(300, 200, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_txt.setFont(font)
        self.time_txt.setObjectName("time txt")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(70, 400, 420, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")

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

        self.generate.clicked.connect(self.dual_funct)
        self.generate2.clicked.connect(self.filegen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uppercase.setText(_translate("MainWindow", "UpperCase"))
        self.specialcharacter.setText(_translate("MainWindow", "Special Characters"))
        self.number_box.setText(_translate("MainWindow", "Numbers"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.generate2.setText(_translate("MainWindow","Generate to file"))
        self.label1.setText(_translate("MainWindow", "How many digits do you want?"))
        self.label2.setText(_translate("MainWindow", "do you want more than 1? (generates to a file)"))
        self.time_txt.setText(_translate("MainWindow", "Estimated time needed to crack the password:"))

    def dual_funct(self):
        self.label.setText(self.generatepw())
        self.estimate.setText(str(self.estimate_time()) + " seconds")
    def generatepw(self):
        from random import sample, randint
        lower = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"}
        upper = {i.upper() for i in lower}
        special = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "{", "}", "[", "]", "|", ";", ":",
                   "'", '"', ",", "<", ".", ">", "/", "?", "`", "~"}
        number = {1,2,3,4,5,6,7,8,9,0}
        password = ""
        pw = []

        upper_check = self.uppercase.isChecked()

        special_check = self.specialcharacter.isChecked()
        numcheck = self.number_box.isChecked()
        try:
            while len(pw) < int(self.lenght.text()):
                num = randint(1, 4)
                if num == 1:
                    if special_check == True:
                        pw.append(sample(special, 1)[0])
                if num == 2:
                    if upper_check == True:
                        pw.append(sample(upper, 1)[0])
                if num == 3:
                    pw.append(sample(lower, 1)[0])
                if num == 4:
                    if numcheck == True:
                        pw.append(sample(number, 1)[0])
            self.estimate_time()
        except:
            QMessageBox.warning(self.window,"Generation Error", " Something went wrong please check your input and try again",
                            QMessageBox.Ok)
            self.lenght.setText("")
        for x in pw:
            password = password + str(x)
        return password

    def filegen(self):
        import os
        try:
            x = int(self.times.text())
            n = 0
            with open("password.txt", "w+") as f:
                f.write("Please Change the file name before regenerating password if you want the file to be saved.\n")
                while n < x :
                    n += 1
                    f.write(str(n) +": " + str(self.generatepw()) + "   Estimated Time to crack: " + str(self.estimate_time()))
                    f.write("\n")

            os.system("password.txt")
        except:
            QMessageBox.warning(self.window, "Generation Error", " Something went wrong please check your input and try again",
                            QMessageBox.Ok)
            self.times.setText("")

    def estimate_time(self):
        num = 26
        password = self.label.text()
        uppercase = self.uppercase.isChecked()
        special = self.specialcharacter.isChecked()
        number = self.number_box.isChecked()

        if number == True:
            num += 10
        if special == True:
            num += 30
        if uppercase == True:
            num += 26

        possible = num ** len(password)
        seconds = possible / 350000000000  # 350 billion

        return seconds


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
