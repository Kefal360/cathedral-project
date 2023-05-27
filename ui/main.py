# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1185, 622)
        MainWindow.setMinimumSize(QtCore.QSize(1185, 622))
        MainWindow.setMaximumSize(QtCore.QSize(1185, 622))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1050, 10, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 51, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 10, 981, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(550, 190, 141, 41))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setProperty("value", 5.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 190, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(540, 470, 81, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setStyleSheet("QLCDNumber { color: black; }")
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("value", 5.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(620, 470, 81, 20))
        self.lcdNumber_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setProperty("value", 5.0)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(700, 470, 81, 20))
        self.lcdNumber_4.setSmallDecimalPoint(False)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 500, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(650, 500, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(730, 500, 47, 13))
        self.label_9.setObjectName("label_9")
        self.off_1 = QtWidgets.QLabel(self.centralwidget)
        self.off_1.setGeometry(QtCore.QRect(804, 100, 61, 51))
        self.off_1.setText("")
        self.off_1.setPixmap(QtGui.QPixmap(":/img/off.svg"))
        self.off_1.setScaledContents(True)
        self.off_1.setObjectName("off_1")
        self.on_1 = QtWidgets.QLabel(self.centralwidget)
        self.on_1.setGeometry(QtCore.QRect(804, 100, 61, 51))
        self.on_1.setText("")
        self.on_1.setPixmap(QtGui.QPixmap(":/img/ON.svg"))
        self.on_1.setScaledContents(True)
        self.on_1.setObjectName("on_1")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(390, 70, 61, 61))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(":/img/led_on.svg"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setEnabled(True)
        self.label_24.setGeometry(QtCore.QRect(390, 70, 61, 61))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap(":/img/led_off.svg"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 140, 71, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 140, 71, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(480, 70, 61, 61))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap(":/img/led_on.svg"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(480, 70, 61, 61))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap(":/img/led_off.svg"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 140, 71, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(570, 70, 61, 61))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap(":/img/led_on.svg"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(570, 70, 61, 61))
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap(":/img/led_off.svg"))
        self.label_31.setScaledContents(True)
        self.label_31.setObjectName("label_31")
        self.off_2 = QtWidgets.QLabel(self.centralwidget)
        self.off_2.setGeometry(QtCore.QRect(904, 100, 61, 51))
        self.off_2.setText("")
        self.off_2.setPixmap(QtGui.QPixmap(":/img/off.svg"))
        self.off_2.setScaledContents(True)
        self.off_2.setObjectName("off_2")
        self.on_2 = QtWidgets.QLabel(self.centralwidget)
        self.on_2.setGeometry(QtCore.QRect(904, 100, 61, 51))
        self.on_2.setText("")
        self.on_2.setPixmap(QtGui.QPixmap(":/img/ON.svg"))
        self.on_2.setScaledContents(True)
        self.on_2.setObjectName("on_2")
        self.off_3 = QtWidgets.QLabel(self.centralwidget)
        self.off_3.setGeometry(QtCore.QRect(994, 100, 61, 51))
        self.off_3.setText("")
        self.off_3.setPixmap(QtGui.QPixmap(":/img/off.svg"))
        self.off_3.setScaledContents(True)
        self.off_3.setObjectName("off_3")
        self.on_3 = QtWidgets.QLabel(self.centralwidget)
        self.on_3.setGeometry(QtCore.QRect(994, 100, 61, 51))
        self.on_3.setText("")
        self.on_3.setPixmap(QtGui.QPixmap(":/img/ON.svg"))
        self.on_3.setScaledContents(True)
        self.on_3.setObjectName("on_3")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(310, 260, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lcd_pressure = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_pressure.setGeometry(QtCore.QRect(550, 260, 141, 41))
        self.lcd_pressure.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_pressure.setProperty("value", 5.0)
        self.lcd_pressure.setObjectName("lcd_pressure")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(550, 330, 141, 41))
        self.lcdNumber_7.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_7.setProperty("value", 5.0)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(310, 330, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setGeometry(QtCore.QRect(550, 400, 141, 41))
        self.lcdNumber_8.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_8.setProperty("value", 5.0)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(310, 400, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(310, 520, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.vkl_b = QtWidgets.QPushButton(self.centralwidget)
        self.vkl_b.setGeometry(QtCore.QRect(1099, 482, 75, 23))
        self.vkl_b.setObjectName("vkl_b")
        self.vikl_b = QtWidgets.QPushButton(self.centralwidget)
        self.vikl_b.setGeometry(QtCore.QRect(1099, 512, 75, 23))
        self.vikl_b.setObjectName("vikl_b")
        self.color_b = QtWidgets.QPushButton(self.centralwidget)
        self.color_b.setGeometry(QtCore.QRect(1099, 542, 75, 23))
        self.color_b.setObjectName("color_b")
        self.leds1 = QtWidgets.QLabel(self.centralwidget)
        self.leds1.setGeometry(QtCore.QRect(1130, 183, 16, 16))
        self.leds1.setMouseTracking(False)
        self.leds1.setTabletTracking(True)
        self.leds1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leds1.setAutoFillBackground(False)
        self.leds1.setStyleSheet("QLabel:pressed \n"
" {\n"
"    border: 2px solid red;\n"
"}")
        self.leds1.setFrameShape(QtWidgets.QFrame.Panel)
        self.leds1.setText("")
        self.leds1.setObjectName("leds1")
        self.leds2 = QtWidgets.QLabel(self.centralwidget)
        self.leds2.setGeometry(QtCore.QRect(1130, 221, 16, 16))
        self.leds2.setAutoFillBackground(True)
        self.leds2.setFrameShape(QtWidgets.QFrame.Panel)
        self.leds2.setText("")
        self.leds2.setObjectName("leds2")
        self.leds3 = QtWidgets.QLabel(self.centralwidget)
        self.leds3.setGeometry(QtCore.QRect(1130, 259, 16, 16))
        self.leds3.setAutoFillBackground(True)
        self.leds3.setFrameShape(QtWidgets.QFrame.Panel)
        self.leds3.setText("")
        self.leds3.setObjectName("leds3")
        self.leds4 = QtWidgets.QLabel(self.centralwidget)
        self.leds4.setGeometry(QtCore.QRect(1130, 297, 16, 16))
        self.leds4.setAutoFillBackground(True)
        self.leds4.setFrameShape(QtWidgets.QFrame.Panel)
        self.leds4.setText("")
        self.leds4.setObjectName("leds4")
        self.leds5 = QtWidgets.QLabel(self.centralwidget)
        self.leds5.setGeometry(QtCore.QRect(1130, 336, 16, 16))
        self.leds5.setAutoFillBackground(True)
        self.leds5.setFrameShape(QtWidgets.QFrame.Panel)
        self.leds5.setText("")
        self.leds5.setObjectName("leds5")
        self.leds6 = QtWidgets.QLabel(self.centralwidget)
        self.leds6.setGeometry(QtCore.QRect(1130, 374, 16, 16))
        self.leds6.setAutoFillBackground(True)
        self.leds6.setFrameShape(QtWidgets.QFrame.Panel)
        self.leds6.setText("")
        self.leds6.setObjectName("leds6")
        self.leds7 = QtWidgets.QLabel(self.centralwidget)
        self.leds7.setGeometry(QtCore.QRect(1130, 412, 16, 16))
        self.leds7.setAutoFillBackground(True)
        self.leds7.setFrameShape(QtWidgets.QFrame.Panel)
        self.leds7.setText("")
        self.leds7.setObjectName("leds7")
        self.leds8 = QtWidgets.QLabel(self.centralwidget)
        self.leds8.setGeometry(QtCore.QRect(1130, 450, 16, 16))
        self.leds8.setAutoFillBackground(True)
        self.leds8.setFrameShape(QtWidgets.QFrame.Panel)
        self.leds8.setText("")
        self.leds8.setObjectName("leds8")
        self.plotwidget = QtWidgets.QWidget(self.centralwidget)
        self.plotwidget.setGeometry(QtCore.QRect(740, 190, 351, 251))
        self.plotwidget.setObjectName("plotwidget")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(540, 530, 81, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber_5.setFont(font)
        self.lcdNumber_5.setStyleSheet("QLCDNumber { color: black; }")
        self.lcdNumber_5.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(700, 530, 81, 20))
        self.lcdNumber_6.setSmallDecimalPoint(False)
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_9.setGeometry(QtCore.QRect(620, 530, 81, 20))
        self.lcdNumber_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.lcdNumber_9.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(310, 460, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(570, 560, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(650, 560, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(730, 560, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(900, 60, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 291, 531))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1050, 50, 101, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(790, 40, 241, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1185, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IoT pgrm v0_1_13"))
        self.pushButton.setText(_translate("MainWindow", "SEND Post"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.label_2.setText(_translate("MainWindow", "Body message"))
        self.label_6.setText(_translate("MainWindow", "Температура"))
        self.lcdNumber_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "R"))
        self.label_8.setText(_translate("MainWindow", "G"))
        self.label_9.setText(_translate("MainWindow", "B"))
        self.pushButton_2.setText(_translate("MainWindow", "Вкл"))
        self.pushButton_3.setText(_translate("MainWindow", "Вкл"))
        self.pushButton_4.setText(_translate("MainWindow", "Вкл"))
        self.label_13.setText(_translate("MainWindow", "Давление"))
        self.label_14.setText(_translate("MainWindow", "Освещенность"))
        self.label_15.setText(_translate("MainWindow", "Освещенность"))
        self.label_34.setText(_translate("MainWindow", "Акселлерометр"))
        self.vkl_b.setText(_translate("MainWindow", "Вкл"))
        self.vikl_b.setText(_translate("MainWindow", "Выкл"))
        self.color_b.setText(_translate("MainWindow", "Цвет"))
        self.lcdNumber_5.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "Освещенность"))
        self.label_10.setText(_translate("MainWindow", "Х"))
        self.label_11.setText(_translate("MainWindow", "Y"))
        self.label_12.setText(_translate("MainWindow", "Z"))
        self.label_4.setText(_translate("MainWindow", "Тумблеры"))
        self.pushButton_5.setText(_translate("MainWindow", "SEND Get request"))
import Res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
