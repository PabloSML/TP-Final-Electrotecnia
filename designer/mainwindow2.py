# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1404, 971)
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
        self.frame.setGeometry(QtCore.QRect(94, 680, 1200, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(1200, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1201, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_main = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.horizontalLayout_filter_wrap = QtWidgets.QHBoxLayout()
        self.horizontalLayout_filter_wrap.setObjectName("horizontalLayout_filter_wrap")
        self.filterGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.filterGroupBox.setObjectName("filterGroupBox")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.filterGroupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 293, 166))
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
        self.verticalLayout_filter_values.addLayout(self.horizontalLayout_psy)
        self.horizontalLayout_K = QtWidgets.QHBoxLayout()
        self.horizontalLayout_K.setObjectName("horizontalLayout_K")
        self.comboBox_KG = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.comboBox_KG.setObjectName("comboBox_KG")
        self.comboBox_KG.addItem("")
        self.comboBox_KG.addItem("")
        self.horizontalLayout_K.addWidget(self.comboBox_KG)
        self.lineEdit_KG = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_KG.setObjectName("lineEdit_KG")
        self.horizontalLayout_K.addWidget(self.lineEdit_KG)
        self.verticalLayout_filter_values.addLayout(self.horizontalLayout_K)
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
        self.verticalLayout_input_values.addLayout(self.horizontalLayout_f)
        self.horizontalLayout_input.addLayout(self.verticalLayout_input_values)
        self.horizontalLayout_input_wrap.addWidget(self.inputGroupBox)
        self.horizontalLayout_main.addLayout(self.horizontalLayout_input_wrap)
        self.horizontalLayout_plot_wrap = QtWidgets.QHBoxLayout()
        self.horizontalLayout_plot_wrap.setObjectName("horizontalLayout_plot_wrap")
        self.plotGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.plotGroupBox.setObjectName("plotGroupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.plotGroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 211, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_plot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_plot.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_plot.setObjectName("verticalLayout_plot")
        self.plotType = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.plotType.setObjectName("plotType")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.verticalLayout_plot.addWidget(self.plotType)
        self.ampOrFase = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.ampOrFase.setObjectName("ampOrFase")
        self.ampOrFase.addItem("")
        self.ampOrFase.addItem("")
        self.verticalLayout_plot.addWidget(self.ampOrFase)
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
        self.graphics = QtWidgets.QStackedWidget(self.centralwidget)
        self.graphics.setGeometry(QtCore.QRect(90, 20, 1191, 641))
        self.graphics.setObjectName("graphics")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.graphics.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.graphics.addWidget(self.page_2)
        self.horizontalSlider_T = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_T.setGeometry(QtCore.QRect(380, 880, 631, 22))
        self.horizontalSlider_T.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_T.setObjectName("horizontalSlider_T")
        self.horizontalSlider_w = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_w.setGeometry(QtCore.QRect(380, 880, 631, 22))
        self.horizontalSlider_w.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_w.setObjectName("horizontalSlider_w")
        self.horizontalSlider_psy = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_psy.setGeometry(QtCore.QRect(380, 880, 631, 22))
        self.horizontalSlider_psy.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_psy.setObjectName("horizontalSlider_psy")
        self.horizontalSlider_KG = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_KG.setGeometry(QtCore.QRect(380, 880, 631, 22))
        self.horizontalSlider_KG.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_KG.setObjectName("horizontalSlider_KG")
        self.horizontalSlider_A = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_A.setGeometry(QtCore.QRect(380, 880, 631, 22))
        self.horizontalSlider_A.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_A.setObjectName("horizontalSlider_A")
        self.horizontalSlider_f = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_f.setGeometry(QtCore.QRect(380, 880, 631, 22))
        self.horizontalSlider_f.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_f.setObjectName("horizontalSlider_f")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1404, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
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
        self.label_T.setText(_translate("MainWindow", "T"))
        self.label_psy.setText(_translate("MainWindow", "ξ"))
        self.comboBox_KG.setItemText(0, _translate("MainWindow", "K"))
        self.comboBox_KG.setItemText(1, _translate("MainWindow", "G"))
        self.inputGroupBox.setTitle(_translate("MainWindow", "Entrada"))
        self.inputType.setItemText(0, _translate("MainWindow", "Elija Señal..."))
        self.inputType.setItemText(1, _translate("MainWindow", "Senoide"))
        self.inputType.setItemText(2, _translate("MainWindow", "Pulso"))
        self.label_A.setText(_translate("MainWindow", "A"))
        self.label_f.setText(_translate("MainWindow", "f"))
        self.plotGroupBox.setTitle(_translate("MainWindow", "Ploteo"))
        self.plotType.setItemText(0, _translate("MainWindow", "Elija Tipo de Gráfico..."))
        self.plotType.setItemText(1, _translate("MainWindow", "Salida"))
        self.plotType.setItemText(2, _translate("MainWindow", "Bode"))
        self.plotType.setItemText(3, _translate("MainWindow", "Polos/Ceros"))
        self.ampOrFase.setItemText(0, _translate("MainWindow", "Amplitud"))
        self.ampOrFase.setItemText(1, _translate("MainWindow", "Fase"))
        self.simButton.setText(_translate("MainWindow", "Simular"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
