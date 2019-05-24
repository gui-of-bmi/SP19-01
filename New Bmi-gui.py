# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\New Bmi-gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 738)
        MainWindow.setStyleSheet("background-color: rgb(141, 141, 141);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Header_2 = QtWidgets.QFrame(self.centralwidget)
        self.Header_2.setGeometry(QtCore.QRect(0, 0, 860, 60))
        self.Header_2.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.Header_2.setObjectName("Header_2")
        self.Header = QtWidgets.QVBoxLayout(self.Header_2)
        self.Header.setSpacing(8)
        self.Header.setObjectName("Header")
        self.label_7 = QtWidgets.QLabel(self.Header_2)
        self.label_7.setObjectName("label_7")
        self.Header.addWidget(self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 90, 170, 41))
        self.comboBox.setStyleSheet("\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.Gender = QtWidgets.QLabel(self.centralwidget)
        self.Gender.setGeometry(QtCore.QRect(40, 90, 111, 41))
        self.Gender.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.Gender.setObjectName("Gender")
        self.Age_2 = QtWidgets.QLabel(self.centralwidget)
        self.Age_2.setGeometry(QtCore.QRect(40, 160, 111, 41))
        self.Age_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.Age_2.setObjectName("Age_2")
        self.Height = QtWidgets.QLabel(self.centralwidget)
        self.Height.setGeometry(QtCore.QRect(40, 300, 110, 41))
        self.Height.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.Height.setObjectName("Height")
        self.Height_feet = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Height_feet.setGeometry(QtCore.QRect(170, 300, 170, 40))
        self.Height_feet.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.Height_feet.setObjectName("Height_feet")
        self.Weight_2 = QtWidgets.QLabel(self.centralwidget)
        self.Weight_2.setGeometry(QtCore.QRect(40, 230, 110, 41))
        self.Weight_2.setStyleSheet("\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.Weight_2.setObjectName("Weight_2")
        self.BMI = QtWidgets.QLabel(self.centralwidget)
        self.BMI.setGeometry(QtCore.QRect(680, 110, 111, 30))
        self.BMI.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.BMI.setObjectName("BMI")
        self.BMI_Result = QtWidgets.QTextEdit(self.centralwidget)
        self.BMI_Result.setGeometry(QtCore.QRect(630, 160, 200, 40))
        self.BMI_Result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.BMI_Result.setObjectName("BMI_Result")
        self.Ideal_Weight = QtWidgets.QTextEdit(self.centralwidget)
        self.Ideal_Weight.setGeometry(QtCore.QRect(630, 280, 210, 40))
        self.Ideal_Weight.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.Ideal_Weight.setObjectName("Ideal_Weight")
        self.Ideal_weight = QtWidgets.QLabel(self.centralwidget)
        self.Ideal_weight.setGeometry(QtCore.QRect(620, 220, 230, 30))
        self.Ideal_weight.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"")
        self.Ideal_weight.setObjectName("Ideal_weight")
        self.Result_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Result_text.setGeometry(QtCore.QRect(630, 510, 200, 100))
        self.Result_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.Result_text.setObjectName("Result_text")
        self.Analyzer = QtWidgets.QTextEdit(self.centralwidget)
        self.Analyzer.setGeometry(QtCore.QRect(40, 470, 500, 210))
        self.Analyzer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.Analyzer.setObjectName("Analyzer")
        self.Result = QtWidgets.QLabel(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(640, 460, 170, 40))
        self.Result.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.Result.setObjectName("Result")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 380, 411, 41))
        self.pushButton.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"font-weight:600; color:#ffdf5c;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 160, 361, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 300, 171, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 230, 171, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.Height_2 = QtWidgets.QLabel(self.centralwidget)
        self.Height_2.setGeometry(QtCore.QRect(350, 300, 200, 41))
        self.Height_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.Height_2.setObjectName("Height_2")
        self.Height_3 = QtWidgets.QLabel(self.centralwidget)
        self.Height_3.setGeometry(QtCore.QRect(350, 230, 240, 41))
        self.Height_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.Height_3.setObjectName("Height_3")
        self.Height_4 = QtWidgets.QLabel(self.centralwidget)
        self.Height_4.setGeometry(QtCore.QRect(640, 250, 190, 20))
        self.Height_4.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.Height_4.setObjectName("Height_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 620, 200, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"font-weight:600; color:#ffdf5c;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.Ideal_Height = QtWidgets.QTextEdit(self.centralwidget)
        self.Ideal_Height.setGeometry(QtCore.QRect(630, 400, 210, 40))
        self.Ideal_Height.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.Ideal_Height.setObjectName("Ideal_Height")
        self.Ideal_weight_2 = QtWidgets.QLabel(self.centralwidget)
        self.Ideal_weight_2.setGeometry(QtCore.QRect(620, 340, 230, 30))
        self.Ideal_weight_2.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"")
        self.Ideal_weight_2.setObjectName("Ideal_weight_2")
        self.Height_5 = QtWidgets.QLabel(self.centralwidget)
        self.Height_5.setGeometry(QtCore.QRect(640, 370, 190, 20))
        self.Height_5.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.Height_5.setObjectName("Height_5")
        self.lineEdit_4.raise_()
        self.lineEdit.raise_()
        self.Header_2.raise_()
        self.comboBox.raise_()
        self.Gender.raise_()
        self.Age_2.raise_()
        self.Height.raise_()
        self.Height_feet.raise_()
        self.Weight_2.raise_()
        self.BMI.raise_()
        self.BMI_Result.raise_()
        self.Ideal_Weight.raise_()
        self.Ideal_weight.raise_()
        self.Result_text.raise_()
        self.Analyzer.raise_()
        self.Result.raise_()
        self.pushButton.raise_()
        self.lineEdit_2.raise_()
        self.Height_2.raise_()
        self.Height_3.raise_()
        self.Height_4.raise_()
        self.pushButton_2.raise_()
        self.Ideal_Height.raise_()
        self.Ideal_weight_2.raise_()
        self.Height_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.try_text)
        self.pushButton_2.clicked.connect(self.graph)

    def graph(self):
            
            import matplotlib.pyplot as plt
            left_edges = [5, 10, 20, 30, 40]
            heights = [100, 200, 300, 400, 500]
            bar_width = 5 
            plt.bar(left_edges, heights, bar_width)
            plt.show()


                
        
    def try_text(self):
        height=float(self.lineEdit_2.text())
        height_in_meter= height*12*0.025
        weight=float(self.lineEdit_4.text())
        bmi = weight / (height_in_meter**2)
        bmi=round(bmi,2)
        self.BMI_Result.setText(str(bmi))
        print ("BMI Is: " , str(bmi))
        age_tt=int(self.lineEdit.text())

        if self.comboBox.currentIndex():
                if str(age_tt) <= str(20):
                        self.Ideal_Weight.setText(str("40 Kg. to 50 Kg."))
                        self.Ideal_Height.setText(str("4.0 ft to 5.5 ft"))
                elif str(age_tt) <= str(30):
                        self.Ideal_Weight.setText(str("50 Kg. to 60 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
                elif str(age_tt) <= str(40):
                        self.Ideal_Weight.setText(str("60 Kg. to 65 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
                elif str(age_tt) <= str(50):
                        self.Ideal_Weight.setText(str("65 Kg. to 68 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
                elif str(age_tt) <= str(60):
                        self.Ideal_Weight.setText(str("68 Kg. to 71 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
                elif str(age_tt) <= str(70):
                        self.Ideal_Weight.setText(str("65 Kg. to 68 Kg."))
                        self.Ideal_Height.setText(str("5.5 ft to 5.9 ft"))
        else:
                if str(age_tt) <= str(20):
                        self.Ideal_Weight.setText(str("45 Kg. to 58 Kg."))
                        self.Ideal_Height.setText(str("4.9 ft to 5.5 ft"))
                elif str(age_tt) <= str(30):
                        self.Ideal_Weight.setText(str("59 Kg. to 70 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
                elif str(age_tt) <= str(40):
                        self.Ideal_Weight.setText(str("70 Kg. to 73 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
                elif str(age_tt) <= str(50):
                        self.Ideal_Weight.setText(str("73 Kg. to 75 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
                elif str(age_tt) <= str(60):
                        self.Ideal_Weight.setText(str("75 Kg. to 77 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
                elif str(age_tt) <= str(70):
                        self.Ideal_Weight.setText(str("75 Kg. to 77 Kg."))
                        self.Ideal_Height.setText(str("5.0 ft to 6.0 ft"))
        

        
        
        
        
        if str(bmi) < str(15):
                self.Result_text.setText(str("You are very severely underweight")) 
        elif str(bmi) <= str(18.5):
                self.Result_text.setText(str("severely underweight")) 
        elif str(bmi) <= str(25):
                self.Result_text.setText(str("You are Normal (healthy weight)"))
        elif str(bmi) <= str(30):
                self.Result_text.setText(str(" You are overweight."))
        elif str(bmi) <= str(35):
                self.Result_text.setText(str(" You are moderately obese."))
        elif str(bmi) <= str(40):
                self.Result_text.setText(str(" You are severely obese."))
        elif str(bmi) > str(40):
                self.Result_text.setText(str(" You are very severely obese."))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffdf5c;\">BMI CALCULATOR AND ANALYZER</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.Gender.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffdf5c;\">GENDER :</span></p></body></html>"))
        self.Age_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffdf5c;\">AGE :</span></p></body></html>"))
        self.Height.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffdf5c;\">HEIGHT :</span></p></body></html>"))
        self.Weight_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffdf5c;\">WEIGHT :</span></p></body></html>"))
        self.BMI.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffdf5c;\">BMI :</span></p></body></html>"))
        self.BMI_Result.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Ideal_Weight.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Ideal_weight.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffdf5c;\">IDEAL WEIGHT:</span></p></body></html>"))
        self.Result_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.Analyzer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.Result.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffdf5c;\">RESULT:</span></p></body></html>"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#ffdf5c;\">Calculate BMI</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Calculate BMI"))
        self.Height_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffdf5c;\">(Height in Feet.Inches)</span></p></body></html>"))
        self.Height_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffdf5c;\">(Weight In Kilgogram or Kg.)</span></p></body></html>"))
        self.Height_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffdf5c;\">(According To Your AGE)</span></p></body></html>"))
        self.pushButton_2.setWhatsThis(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#ffdf5c;\">Calculate BMI</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Analyze"))
        self.Ideal_Height.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Ideal_weight_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffdf5c;\">IDEAL HEIGHT:</span></p></body></html>"))
        self.Height_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffdf5c;\">(According To Your AGE)</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

