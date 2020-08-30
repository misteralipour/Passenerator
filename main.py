import re
import os
import sys
import time
import random
# import subprocess
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 10, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 40, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(310, 70, 61, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(400, 40, 201, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 70, 201, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(310, 40, 81, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(400, 70, 201, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(40, 371, 561, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 341, 511, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(310, 100, 291, 21))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 591, 201))
        self.textEdit.setObjectName("textEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(90, 100, 201, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(16, 10, 591, 381))
        font = QtGui.QFont()
        font.setFamily("Jellee Roman")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.generate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def generate(self):
        first_name = self.lineEdit.text()
        last_name = self.lineEdit_2.text()
        id_no = self.lineEdit_3.text()
        phone_no = self.lineEdit_4.text()
        country = self.lineEdit_5.text()
        city = self.lineEdit_6.text()
        simple_birth = self.dateEdit.text()
        birth = re.sub("[^\w]", " ",  simple_birth).split()
        day = birth[0]
        month = birth[1]
        year = birth[2]
        others = self.textEdit.toPlainText()
        othersList = re.sub("[^\w]", " ",  others).split()
        infoList = [first_name, last_name, id_no, phone_no, country, city, day, month, year]
        ninfoList = []

        for word in infoList:
            ninfoList.append(word.upper())
            if 'a' in word: ninfoList.append(word.replace("a", "@"))
            if 'b' in word: ninfoList.append(word.replace("b", "4"))
            if 'e' in word: ninfoList.append(word.replace("e", "3"))
            if 'o' in word: ninfoList.append(word.replace("o", "0"))
            if 'h' in word: ninfoList.append(word.replace("h", "8"))
            if 'i' in word: ninfoList.append(word.replace("i", "1"))

        data = othersList + infoList + ninfoList

        # self.progressBar.setValue(50)

        f = open("passwords.txt", "w")

        for i in range(100):
            output = ''.join(random.sample(data, random.randint(1, 3)))
            if len(output) > 6:
                f.write(output+'\n')
            # f.write(''.join(random.sample(data, random.randint(1, 3)))+'\n')
            self.progressBar.setValue(i+1)

        # self.progressBar.setValue(100)
        self.lineEdit_7.setText('Information: passwords saved to passwords.txt!')

        os.startfile('passwords.txt')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Passenerator"))
        self.pushButton.setText(_translate("MainWindow", "Generate!"))
        self.label.setText(_translate("MainWindow", "First Name:"))
        self.label_2.setText(_translate("MainWindow", "Last Name:"))
        self.label_3.setText(_translate("MainWindow", "ID Number:"))
        self.label_4.setText(_translate("MainWindow", "Born City:"))
        self.label_5.setText(_translate("MainWindow", "Born Country:"))
        self.label_6.setText(_translate("MainWindow", "Phone Number:"))
        self.lineEdit_7.setText(_translate("MainWindow", "Information: "))
        self.label_8.setText(_translate("MainWindow", "Enter Any Other Words Like Guessed Passes Separate via ,"))
        self.label_9.setText(_translate("MainWindow", "Birthday:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">This Software Make Passwords Based On Person\'s Information.</p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">By: Mr A</span></p><p align=\"center\"><a href=\"https://github.com/misteralipour\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/misteralipour</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())