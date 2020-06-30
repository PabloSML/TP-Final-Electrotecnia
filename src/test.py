# Qt Modules
#from src.ui.mainwindow import Ui_MainWindow
from src.ui.mainwindow2 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import src.backend as bck

# Matplotlib Modules
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# # Python Module       BORRAR SI NO SE USA
# import numpy as np
# from scipy import signal

class myWidget (QMainWindow, Ui_MainWindow):

    # INIT
    def __init__(self):
        super().__init__()

        #Initial setup
        self.setupUi(self)
        self.setWindowTitle("SIMBA")

        #Hide assets for first use
        self.hide_order_one()
        self.hide_order_two()
        self.hide_pulse_input()
        self.hide_sin_input()

        # # Creates figure and canvas.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.canvas, self)

        plot_layout = QtWidgets.QVBoxLayout()
        plot_layout.addWidget(toolbar)
        plot_layout.addWidget(self.canvas)

        plot_widget = QtWidgets.QWidget()
        plot_widget.setLayout(plot_layout)

        # Sets current index in canvas to show plot.
        canvas_index = self.graphics.addWidget(plot_widget)
        self.graphics.setCurrentIndex(canvas_index)

        # # Adds axes to figure.
        self.axes = self.figure.add_subplot()

        #Connections to callbacks
        self.filterOrder.currentIndexChanged.connect(self.order_change)
        self.inputType.currentIndexChanged.connect(self.input_change)
        self.simButton.pressed.connect(self.testBackend)

    #METODOS DE UI VISUALES

    def hide_order_one(self):
        self.filterType.setCurrentIndex(0)
        self.filterType.hide()
        self.label_T.hide()
        self.lineEdit_T.clear()
        self.lineEdit_T.hide()
        self.unitsDDown_T.setCurrentIndex(0)
        self.unitsDDown_T.hide()
        self.label_K.hide()
        self.lineEdit_K.clear()
        self.lineEdit_K.hide()
        self.unitsDDown_K.setCurrentIndex(0)
        self.unitsDDown_K.hide()
        self.label_G.hide()
        self.lineEdit_G.clear()
        self.lineEdit_G.hide()
        self.unitsDDown_G.setCurrentIndex(0)
        self.unitsDDown_G.hide()

        if self.simButton.isChecked():
            self.simButton.toggle()

    def show_order_one(self):
        self.filterType.show()
        self.label_T.show()
        self.lineEdit_T.show()
        self.unitsDDown_T.show()
        self.label_K.show()
        self.lineEdit_K.show()
        self.unitsDDown_K.show()
        self.label_G.show()
        self.lineEdit_G.show()
        self.unitsDDown_G.show()

    def hide_order_two(self):
        self.filterType2.setCurrentIndex(0)
        self.filterType2.hide()
        self.label_w.hide()
        self.label_psy.hide()
        self.lineEdit_w.clear()
        self.lineEdit_w.hide()
        self.lineEdit_psy.clear()
        self.lineEdit_psy.hide()
        self.unitsDDown_w.setCurrentIndex(0)
        self.unitsDDown_w.hide()
        self.unitsDDown_psy.setCurrentIndex(0)
        self.unitsDDown_psy.hide()
        self.label_K.hide()
        self.lineEdit_K.clear()
        self.lineEdit_K.hide()
        self.unitsDDown_K.setCurrentIndex(0)
        self.unitsDDown_K.hide()
        self.label_G.hide()
        self.lineEdit_G.clear()
        self.lineEdit_G.hide()
        self.unitsDDown_G.setCurrentIndex(0)
        self.unitsDDown_G.hide()

        if self.simButton.isChecked():
            self.simButton.toggle()

    def show_order_two(self):
        self.filterType2.show()
        self.label_w.show()
        self.label_psy.show()
        self.lineEdit_w.show()
        self.lineEdit_psy.show()
        self.unitsDDown_w.show()
        self.unitsDDown_psy.show()
        self.label_K.show()
        self.lineEdit_K.show()
        self.unitsDDown_K.show()
        self.label_G.show()
        self.lineEdit_G.show()
        self.unitsDDown_G.show()

    def order_change(self):
        if self.filterOrder.currentIndex() == 1:
            self.hide_order_two()
            self.show_order_one()

        elif self.filterOrder.currentIndex() == 2:
            self.hide_order_one()
            self.show_order_two()

        else:
            self.hide_order_one()
            self.hide_order_two()

    def hide_pulse_input(self):
        self.label_A.hide()
        self.lineEdit_A.clear()
        self.lineEdit_A.hide()
        self.unitsDDown_A.setCurrentIndex(0)
        self.unitsDDown_A.hide()

        if self.simButton.isChecked():
            self.simButton.toggle()

    def show_pulse_input(self):
        self.label_A.show()
        self.lineEdit_A.show()
        self.unitsDDown_A.show()

    def hide_sin_input(self):
        self.label_A.hide()
        self.label_f.hide()
        self.lineEdit_A.clear()
        self.lineEdit_A.hide()
        self.lineEdit_f.clear()
        self.lineEdit_f.hide()
        self.unitsDDown_A.setCurrentIndex(0)
        self.unitsDDown_A.hide()
        self.unitsDDown_f.setCurrentIndex(0)
        self.unitsDDown_f.hide()

        if self.simButton.isChecked():
            self.simButton.toggle()

    def show_sin_input(self):
        self.label_A.show()
        self.label_f.show()
        self.lineEdit_A.show()
        self.lineEdit_f.show()
        self.unitsDDown_A.show()
        self.unitsDDown_f.show()

    def input_change(self):

        if self.inputType.currentIndex() == 1:
            self.hide_pulse_input()
            self.show_sin_input()

        elif self.inputType.currentIndex() == 2:
            self.hide_sin_input()
            self.show_pulse_input()

        else:
            self.hide_pulse_input()
            self.hide_sin_input()

    #METODOS DE UI LOGICOS

    def testBackend(self):
        bck.plotZerosPoles(self, bck.pasabajos(1,1,1))
        #bck.plotBode(self,bck.pasabajos(1,1,1))
        #bck.plotOutput(self,bck.pasabajos(1,1,1),'sin',1,1,np.linspace(0,20,100))

