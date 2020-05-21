# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bank.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from db import *
from PyQt5.QtWidgets import *
import sys

test1=sqlitehelp("test.db")
test1.createtable()

class Ui_bank(QWidget):
    def createanewaccount(self):
        self.stackedWidget.setCurrentIndex(1)
    def balanceenquiry(self):
        self.stackedWidget.setCurrentIndex(4)
    def withdraw(self):
        self.stackedWidget.setCurrentIndex(2)
    def deposit(self):
        self.stackedWidget.setCurrentIndex(3)
    def balancedetail(self):
        a=self.lineEdit_13.text()
        if(not a==""):
            b=test1.select("SELECT * FROM bankusers1 WHERE Accountno='{}'".format(a))
            if b:
                d="Name:"+b[0][0]+"\n"+"ACCNO:"+str(b[0][1])+"\n"+"ACCTYPE:"+b[0][2]+"\n"+"Balance:"+str(b[0][3])
                self.label_14.setText(d)
                print(d)
            else:
                QMessageBox.warning(self,"invalid account no","Please check your account no!")
        else:
            QMessageBox.warning(self,"ALl fields are imprtant","Please fill all the fields!")

        
    def back(self):
        self.stackedWidget.setCurrentIndex(0)     
    def newaccount(self):
        a=self.lineEdit.text()
        b=self.lineEdit_2.text()
        c=(self.lineEdit_3.text().lower())
        d=self.lineEdit_4.text()
        e=test1.select("SELECT * FROM bankusers1 WHERE Accountno='{}'".format(b))
        if(a=="" or b=="" or c=="" or d==""):
            QMessageBox.warning(self,"All fileds are not filled","please fill all the fields!")
        else:
            users9=(a,int(b),c,int(d))
            e=test1.select("SELECT * FROM bankusers1 WHERE Accountno='{}'".format(b))
            if(not e):
                if(c=='saving'or c== 'current'):
                    if(c=='saving'):
                        if(int(d)>=1000):
                            test1.insert(" INSERT INTO bankusers1(Name,Accountno,Accounttype,Amount)VALUES(?,?,?,?)",users9)
                            QMessageBox.information(self,"Account was created succesfully","Account was created succesfully!")
                            self.stackedWidget.setCurrentIndex(0)
                        else:
                            QMessageBox.warning(self,"not sufficent amount","For saving intial deposit should be at least 1000!")
                    else:
                        if(int(d)>=500):
                            test1.insert(" INSERT INTO bankusers1(Name,Accountno,Accounttype,Amount)VALUES(?,?,?,?)",users9)
                            QMessageBox.information(self,"Account was created succesfully","Account was created succesfully!")
                            self.stackedWidget.setCurrentIndex(0)
                        else:
                            QMessageBox.warning(self,"not sufficent amount","For current account intial deposit should be at least 500!")

                else:
                    QMessageBox.warning(self,"info","Account type must be saving or current")

            else:
                QMessageBox.warning(self,"already exists","please select another account no!")

    def amountwithdraw(self):
        a=self.lineEdit_9.text()
        print(a)
        b=self.lineEdit_10.text()
        print(b)
        if (not (a=="" or b=="")):
            c=test1.select("SELECT * FROM bankusers1 WHERE Accountno='{}'".format(a))
            if c:
                if int(c[0][3])>=int(b):
                    d=int(c[0][3])-int(b)
                    e=str(d)
                    test1.update("UPDATE bankusers1 SET Amount='{0}' WHERE Accountno ='{1}'" .format(e,a))
                    QMessageBox.information(self,"withdraw","you hvae withdraw  Rs "+b+"  succesfully!")
                    self.stackedWidget.setCurrentIndex(0)
                else:
                    QMessageBox.warning(self,"withdraw","Your balance is not suuficent!")
            else:
                QMessageBox.warning(self,"invalid account no","pleaase check your account no!")
        else:
            QMessageBox.warning(self,"All fields are not filled","Please fill all the fields!")
            
        
    def amountdeposited(self):
        a=self.lineEdit_11.text()
        print(a)
        b=self.lineEdit_12.text()
        print(b)
        if(not(a==""or b=="")):
            c=test1.select("SELECT * FROM bankusers1 WHERE Accountno='{}'".format(a))
            if c:
                d=int(c[0][3])+int(b)
                e=str(d)
                test1.update("UPDATE bankusers1 SET Amount='{0}' WHERE Accountno ='{1}'" .format(e,a))
                QMessageBox.information(self,"deposited","you hvae deposited  Rs "+b+"  succesfully!")
                self.stackedWidget.setCurrentIndex(0)
            else:
                 QMessageBox.warning(self,"withdraw","please check your account no!")
        else:
             QMessageBox.warning(self,"All fields are not filled","Please fill all the fields!")

        
        
    
    def setupUi(self, bank):
        bank.setObjectName("bank")
        bank.resize(936, 648)
        self.centralwidget = QtWidgets.QWidget(bank)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 121))
        self.label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(60, 154, 255);")
        self.label.setObjectName("label")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 120, 971, 531))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 121, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(60, 120, 281, 91))
        self.pushButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 84, 115);")
        self.pushButton.setObjectName("pushButton")
        #******************************************#
        self.pushButton.clicked.connect(self.createanewaccount)
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 117, 251, 91))
        self.pushButton_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 84, 115);")
        self.pushButton_2.setObjectName("pushButton_2")
        #****************************************************#
        self.pushButton_2.clicked.connect(self.balanceenquiry)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 290, 281, 101))
        self.pushButton_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 84, 115);")
        self.pushButton_3.setObjectName("pushButton_3")
        #****************************************************#
        self.pushButton_3.clicked.connect(self.withdraw)
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 290, 261, 101))
        self.pushButton_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 84, 115);")
        self.pushButton_5.setObjectName("pushButton_5")
        #****************************************************#
        self.pushButton_5.clicked.connect(self.deposit)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setGeometry(QtCore.QRect(240, 50, 341, 281))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Name of the account holder")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Account No")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("Account type(current/saving)")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("intial amount")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        #**********************************************************#
        self.pushButton_9.clicked.connect(self.newaccount)
        self.verticalLayout.addWidget(self.pushButton_9)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.widget1 = QtWidgets.QWidget(self.page_3)
        self.widget1.setGeometry(QtCore.QRect(290, 100, 261, 181))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setPlaceholderText("Account No")
        self.horizontalLayout_5.addWidget(self.lineEdit_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setPlaceholderText("Amount")
        self.horizontalLayout_6.addWidget(self.lineEdit_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_10.setObjectName("pushButton_10")
        #********************************************#
        self.pushButton_10.clicked.connect(self.amountwithdraw)
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.widget2 = QtWidgets.QWidget(self.page_4)
        self.widget2.setGeometry(QtCore.QRect(220, 70, 281, 261))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.widget2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setPlaceholderText("Account No")
        self.horizontalLayout_7.addWidget(self.lineEdit_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.widget2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setPlaceholderText("Amount")
        self.horizontalLayout_8.addWidget(self.lineEdit_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_11.setObjectName("pushButton_11")
        #***************************************************************#
        self.pushButton_11.clicked.connect(self.amountdeposited)
        self.verticalLayout_3.addWidget(self.pushButton_11)
        self.stackedWidget.addWidget(self.page_4)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.widget3 = QtWidgets.QWidget(self.page_9)
        self.widget3.setGeometry(QtCore.QRect(360, 120, 291, 171))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.widget3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setPlaceholderText("Account No")
        self.horizontalLayout_9.addWidget(self.lineEdit_13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget3)
        self.pushButton_12.setObjectName("pushButton_12")
        #***********************************************************#
        self.pushButton_12.clicked.connect(self.balancedetail)
        self.verticalLayout_4.addWidget(self.pushButton_12)
        #**************NEW******************#
        self.pushButton_13 = QtWidgets.QPushButton(self.widget3)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.back)
        self.verticalLayout_4.addWidget(self.pushButton_13)
        #**********END***************************#
        self.stackedWidget.addWidget(self.page_9)
        #***********************************#
        self.label_14 = QtWidgets.QLabel(self.page_9)
        self.label_14.setGeometry(QtCore.QRect(100, 150, 150, 200))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.page_9)
        bank.setCentralWidget(self.centralwidget)

        
        #**************************************#
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_13 = QtWidgets.QLabel(self.page_10)
        self.label_13.setGeometry(QtCore.QRect(330, 170, 371, 221))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.stackedWidget.addWidget(self.page_10)
        bank.setCentralWidget(self.centralwidget)

        self.retranslateUi(bank)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bank)

    def retranslateUi(self, bank):
        _translate = QtCore.QCoreApplication.translate
        bank.setWindowTitle(_translate("bank", "banking work"))
        self.label.setText(_translate("bank", "                          Bank Mangement system"))
        self.pushButton.setText(_translate("bank", "Create a new account"))
        self.pushButton_2.setText(_translate("bank", "Balance enquiry"))
        self.pushButton_3.setText(_translate("bank", "cash withdraw"))
        self.pushButton_5.setText(_translate("bank", "cash deposit"))
        self.label_2.setText(_translate("bank", "Name"))
        self.label_3.setText(_translate("bank", "Account no"))
        self.label_6.setText(_translate("bank", "Account type"))
        self.label_7.setText(_translate("bank", "Deposit "))
        self.pushButton_9.setText(_translate("bank", "Enter"))
        self.label_8.setText(_translate("bank", "Account no"))
        self.label_9.setText(_translate("bank", "Amount"))
        self.pushButton_10.setText(_translate("bank", "Withdraw"))
        self.label_10.setText(_translate("bank", "Account No"))
        self.label_11.setText(_translate("bank", "Amount"))
        self.pushButton_11.setText(_translate("bank", "Deposit"))
        self.label_12.setText(_translate("bank", "Account No"))
        self.pushButton_12.setText(_translate("bank", "Enter"))
        self.pushButton_13.setText(_translate("bank", "Back"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bank = QtWidgets.QMainWindow()
    ui = Ui_bank()
    ui.setupUi(bank)
    bank.show()
    sys.exit(app.exec_())
