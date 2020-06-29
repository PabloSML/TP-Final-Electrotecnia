# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1404, 934)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 680, 1195, 185))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(1195, 185))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1191, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_main = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.horizontalLayout_filter_wrap = QtWidgets.QHBoxLayout()
        self.horizontalLayout_filter_wrap.setObjectName("horizontalLayout_filter_wrap")
        self.filterGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.filterGroupBox.setObjectName("filterGroupBox")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.filterGroupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 30, 281, 111))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_filter = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_filter.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_filter.setObjectName("horizontalLayout_filter")
        self.verticalLayout_filter_ddown = QtWidgets.QVBoxLayout()
        self.verticalLayout_filter_ddown.setObjectName("verticalLayout_filter_ddown")
        self.filterOrder = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.filterOrder.setEditable(False)
        self.filterOrder.setObjectName("filterOrder")
        self.filterOrder.addItem("")
        self.filterOrder.addItem("")
        self.filterOrder.addItem("")
        self.verticalLayout_filter_ddown.addWidget(self.filterOrder)
        self.filterType = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.filterType.setObjectName("filterType")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.verticalLayout_filter_ddown.addWidget(self.filterType)
        self.filterType2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.filterType2.setObjectName("filterType2")
        self.filterType2.addItem("")
        self.filterType2.addItem("")
        self.filterType2.addItem("")
        self.filterType2.addItem("")
        self.filterType2.addItem("")
        self.filterType2.addItem("")
        self.verticalLayout_filter_ddown.addWidget(self.filterType2)
        self.horizontalLayout_filter.addLayout(self.verticalLayout_filter_ddown)
        self.verticalLayout_filter_values = QtWidgets.QVBoxLayout()
        self.verticalLayout_filter_values.setObjectName("verticalLayout_filter_values")
        self.horizontalLayout_w = QtWidgets.QHBoxLayout()
        self.horizontalLayout_w.setObjectName("horizontalLayout_w")
        self.label_w = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_w.setFont(font)
        self.label_w.setObjectName("label_w")
        self.horizontalLayout_w.addWidget(self.label_w)
        self.lineEdit_w = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_w.setObjectName("lineEdit_w")
        self.horizontalLayout_w.addWidget(self.lineEdit_w)
        self.unitsDDown_w = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.unitsDDown_w.setObjectName("unitsDDown_w")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.setItemText(0, "")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.addItem("")
        self.unitsDDown_w.addItem("")
        self.horizontalLayout_w.addWidget(self.unitsDDown_w)
        self.verticalLayout_filter_values.addLayout(self.horizontalLayout_w)
        self.horizontalLayout_T = QtWidgets.QHBoxLayout()
        self.horizontalLayout_T.setObjectName("horizontalLayout_T")
        self.label_T = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_T.setFont(font)
        self.label_T.setObjectName("label_T")
        self.horizontalLayout_T.addWidget(self.label_T)
        self.lineEdit_T = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_T.setObjectName("lineEdit_T")
        self.horizontalLayout_T.addWidget(self.lineEdit_T)
        self.unitsDDown_T = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.unitsDDown_T.setObjectName("unitsDDown_T")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.setItemText(0, "")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.addItem("")
        self.unitsDDown_T.addItem("")
        self.horizontalLayout_T.addWidget(self.unitsDDown_T)
        self.verticalLayout_filter_values.addLayout(self.horizontalLayout_T)
        self.horizontalLayout_psy = QtWidgets.QHBoxLayout()
        self.horizontalLayout_psy.setObjectName("horizontalLayout_psy")
        self.label_psy = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_psy.setFont(font)
        self.label_psy.setObjectName("label_psy")
        self.horizontalLayout_psy.addWidget(self.label_psy)
        self.lineEdit_psy = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_psy.setObjectName("lineEdit_psy")
        self.horizontalLayout_psy.addWidget(self.lineEdit_psy)
        self.unitsDDown_psy = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.unitsDDown_psy.setObjectName("unitsDDown_psy")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.setItemText(0, "")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.addItem("")
        self.unitsDDown_psy.addItem("")
        self.horizontalLayout_psy.addWidget(self.unitsDDown_psy)
        self.verticalLayout_filter_values.addLayout(self.horizontalLayout_psy)
        self.horizontalLayout_filter.addLayout(self.verticalLayout_filter_values)
        self.horizontalLayout_filter_wrap.addWidget(self.filterGroupBox)
        self.horizontalLayout_main.addLayout(self.horizontalLayout_filter_wrap)
        self.horizontalLayout_input_wrap = QtWidgets.QHBoxLayout()
        self.horizontalLayout_input_wrap.setObjectName("horizontalLayout_input_wrap")
        self.inputGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.inputGroupBox.setObjectName("inputGroupBox")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.inputGroupBox)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 40, 251, 91))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_input = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_input.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_input.setObjectName("horizontalLayout_input")
        self.inputType = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        self.inputType.setObjectName("inputType")
        self.inputType.addItem("")
        self.inputType.addItem("")
        self.inputType.addItem("")
        self.horizontalLayout_input.addWidget(self.inputType)
        self.verticalLayout_input_values = QtWidgets.QVBoxLayout()
        self.verticalLayout_input_values.setObjectName("verticalLayout_input_values")
        self.horizontalLayout_A = QtWidgets.QHBoxLayout()
        self.horizontalLayout_A.setObjectName("horizontalLayout_A")
        self.label_A = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_A.setFont(font)
        self.label_A.setObjectName("label_A")
        self.horizontalLayout_A.addWidget(self.label_A)
        self.lineEdit_A = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_A.setObjectName("lineEdit_A")
        self.horizontalLayout_A.addWidget(self.lineEdit_A)
        self.unitsDDown_A = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        self.unitsDDown_A.setObjectName("unitsDDown_A")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.setItemText(0, "")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.addItem("")
        self.unitsDDown_A.addItem("")
        self.horizontalLayout_A.addWidget(self.unitsDDown_A)
        self.verticalLayout_input_values.addLayout(self.horizontalLayout_A)
        self.horizontalLayout_f = QtWidgets.QHBoxLayout()
        self.horizontalLayout_f.setObjectName("horizontalLayout_f")
        self.label_f = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_f.setFont(font)
        self.label_f.setObjectName("label_f")
        self.horizontalLayout_f.addWidget(self.label_f)
        self.lineEdit_f = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_f.setObjectName("lineEdit_f")
        self.horizontalLayout_f.addWidget(self.lineEdit_f)
        self.unitsDDown_f = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        self.unitsDDown_f.setObjectName("unitsDDown_f")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.setItemText(0, "")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.addItem("")
        self.unitsDDown_f.addItem("")
        self.horizontalLayout_f.addWidget(self.unitsDDown_f)
        self.verticalLayout_input_values.addLayout(self.horizontalLayout_f)
        self.horizontalLayout_input.addLayout(self.verticalLayout_input_values)
        self.horizontalLayout_input_wrap.addWidget(self.inputGroupBox)
        self.horizontalLayout_main.addLayout(self.horizontalLayout_input_wrap)
        self.horizontalLayout_plot_wrap = QtWidgets.QHBoxLayout()
        self.horizontalLayout_plot_wrap.setObjectName("horizontalLayout_plot_wrap")
        self.plotGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.plotGroupBox.setObjectName("plotGroupBox")
        self.plotType = QtWidgets.QComboBox(self.plotGroupBox)
        self.plotType.setGeometry(QtCore.QRect(60, 70, 151, 22))
        self.plotType.setObjectName("plotType")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.horizontalLayout_plot_wrap.addWidget(self.plotGroupBox)
        self.horizontalLayout_main.addLayout(self.horizontalLayout_plot_wrap)
        self.horizontalLayout_simButton_wrap = QtWidgets.QHBoxLayout()
        self.horizontalLayout_simButton_wrap.setSpacing(6)
        self.horizontalLayout_simButton_wrap.setObjectName("horizontalLayout_simButton_wrap")
        self.simButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.simButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.simButton.setFont(font)
        self.simButton.setObjectName("simButton")
        self.horizontalLayout_simButton_wrap.addWidget(self.simButton)
        self.horizontalLayout_main.addLayout(self.horizontalLayout_simButton_wrap)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(90, 40, 1191, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1404, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIMBA"))
        self.filterGroupBox.setTitle(_translate("MainWindow", "Filtros"))
        self.filterOrder.setCurrentText(_translate("MainWindow", "Elija Orden..."))
        self.filterOrder.setItemText(0, _translate("MainWindow", "Elija Orden..."))
        self.filterOrder.setItemText(1, _translate("MainWindow", "Primer Orden"))
        self.filterOrder.setItemText(2, _translate("MainWindow", "Segundo Orden"))
        self.filterType.setItemText(0, _translate("MainWindow", "Elija Tipo..."))
        self.filterType.setItemText(1, _translate("MainWindow", "Pasa Bajos"))
        self.filterType.setItemText(2, _translate("MainWindow", "Pasa Altos"))
        self.filterType.setItemText(3, _translate("MainWindow", "Pasa Todo"))
        self.filterType2.setItemText(0, _translate("MainWindow", "Elija Tipo..."))
        self.filterType2.setItemText(1, _translate("MainWindow", "Pasa Bajos"))
        self.filterType2.setItemText(2, _translate("MainWindow", "Pasa Altos"))
        self.filterType2.setItemText(3, _translate("MainWindow", "Pasa Todo"))
        self.filterType2.setItemText(4, _translate("MainWindow", "Pasa Banda"))
        self.filterType2.setItemText(5, _translate("MainWindow", "Notch"))
        self.label_w.setText(_translate("MainWindow", "ω"))
        self.unitsDDown_w.setItemText(1, _translate("MainWindow", "f"))
        self.unitsDDown_w.setItemText(2, _translate("MainWindow", "p"))
        self.unitsDDown_w.setItemText(3, _translate("MainWindow", "n"))
        self.unitsDDown_w.setItemText(4, _translate("MainWindow", "u"))
        self.unitsDDown_w.setItemText(5, _translate("MainWindow", "m"))
        self.unitsDDown_w.setItemText(6, _translate("MainWindow", "-"))
        self.unitsDDown_w.setItemText(7, _translate("MainWindow", "K"))
        self.unitsDDown_w.setItemText(8, _translate("MainWindow", "M"))
        self.unitsDDown_w.setItemText(9, _translate("MainWindow", "G"))
        self.unitsDDown_w.setItemText(10, _translate("MainWindow", "T"))
        self.label_T.setText(_translate("MainWindow", "T"))
        self.unitsDDown_T.setItemText(1, _translate("MainWindow", "f"))
        self.unitsDDown_T.setItemText(2, _translate("MainWindow", "p"))
        self.unitsDDown_T.setItemText(3, _translate("MainWindow", "n"))
        self.unitsDDown_T.setItemText(4, _translate("MainWindow", "u"))
        self.unitsDDown_T.setItemText(5, _translate("MainWindow", "m"))
        self.unitsDDown_T.setItemText(6, _translate("MainWindow", "-"))
        self.unitsDDown_T.setItemText(7, _translate("MainWindow", "K"))
        self.unitsDDown_T.setItemText(8, _translate("MainWindow", "M"))
        self.unitsDDown_T.setItemText(9, _translate("MainWindow", "G"))
        self.unitsDDown_T.setItemText(10, _translate("MainWindow", "T"))
        self.label_psy.setText(_translate("MainWindow", "ξ"))
        self.unitsDDown_psy.setItemText(1, _translate("MainWindow", "f"))
        self.unitsDDown_psy.setItemText(2, _translate("MainWindow", "p"))
        self.unitsDDown_psy.setItemText(3, _translate("MainWindow", "n"))
        self.unitsDDown_psy.setItemText(4, _translate("MainWindow", "u"))
        self.unitsDDown_psy.setItemText(5, _translate("MainWindow", "m"))
        self.unitsDDown_psy.setItemText(6, _translate("MainWindow", "-"))
        self.unitsDDown_psy.setItemText(7, _translate("MainWindow", "K"))
        self.unitsDDown_psy.setItemText(8, _translate("MainWindow", "M"))
        self.unitsDDown_psy.setItemText(9, _translate("MainWindow", "G"))
        self.unitsDDown_psy.setItemText(10, _translate("MainWindow", "T"))
        self.inputGroupBox.setTitle(_translate("MainWindow", "Entrada"))
        self.inputType.setItemText(0, _translate("MainWindow", "Elija Señal..."))
        self.inputType.setItemText(1, _translate("MainWindow", "Senoide"))
        self.inputType.setItemText(2, _translate("MainWindow", "Pulso"))
        self.label_A.setText(_translate("MainWindow", "A"))
        self.unitsDDown_A.setItemText(1, _translate("MainWindow", "f"))
        self.unitsDDown_A.setItemText(2, _translate("MainWindow", "p"))
        self.unitsDDown_A.setItemText(3, _translate("MainWindow", "n"))
        self.unitsDDown_A.setItemText(4, _translate("MainWindow", "u"))
        self.unitsDDown_A.setItemText(5, _translate("MainWindow", "m"))
        self.unitsDDown_A.setItemText(6, _translate("MainWindow", "-"))
        self.unitsDDown_A.setItemText(7, _translate("MainWindow", "K"))
        self.unitsDDown_A.setItemText(8, _translate("MainWindow", "M"))
        self.unitsDDown_A.setItemText(9, _translate("MainWindow", "G"))
        self.unitsDDown_A.setItemText(10, _translate("MainWindow", "T"))
        self.label_f.setText(_translate("MainWindow", "f"))
        self.unitsDDown_f.setItemText(1, _translate("MainWindow", "f"))
        self.unitsDDown_f.setItemText(2, _translate("MainWindow", "p"))
        self.unitsDDown_f.setItemText(3, _translate("MainWindow", "n"))
        self.unitsDDown_f.setItemText(4, _translate("MainWindow", "u"))
        self.unitsDDown_f.setItemText(5, _translate("MainWindow", "m"))
        self.unitsDDown_f.setItemText(6, _translate("MainWindow", "-"))
        self.unitsDDown_f.setItemText(7, _translate("MainWindow", "K"))
        self.unitsDDown_f.setItemText(8, _translate("MainWindow", "M"))
        self.unitsDDown_f.setItemText(9, _translate("MainWindow", "G"))
        self.unitsDDown_f.setItemText(10, _translate("MainWindow", "T"))
        self.plotGroupBox.setTitle(_translate("MainWindow", "Ploteo"))
        self.plotType.setItemText(0, _translate("MainWindow", "Elija Tipo de Gráfico..."))
        self.plotType.setItemText(1, _translate("MainWindow", "Salida"))
        self.plotType.setItemText(2, _translate("MainWindow", "Bode"))
        self.plotType.setItemText(3, _translate("MainWindow", "Polos/Ceros"))
        self.simButton.setText(_translate("MainWindow", "Simular"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
