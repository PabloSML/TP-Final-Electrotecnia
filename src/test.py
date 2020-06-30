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
import numpy as np
# from scipy import signal


class myWidget (QMainWindow, Ui_MainWindow):

    # INIT
    def __init__(self):
        super().__init__()

        #Initial setup
        self.setupUi(self)
        self.setWindowTitle("SIMBA")
        self.simButton.setCheckable(True)

        self.data = {
            "filterOrder": None,
            "filterType": None,
            "inputType": None,
            "plotType": None,
            "T": None,
            "w": None,
            "psy": None,
            "K": None,
            "A": None,
            "f": None
        }

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

        # Connections to callbacks
        # New filter order chosen
        self.filterOrder.currentIndexChanged.connect(self.order_change)
        # Switched between K and G
        self.comboBox_KG.currentIndexChanged.connect(self.kgChange)
        # New input type chosen
        self.inputType.currentIndexChanged.connect(self.input_change)
        # Intro pressed on data field
        self.lineEdit_T.returnPressed.connect(self.collectData)
        self.lineEdit_w.returnPressed.connect(self.collectData)
        self.lineEdit_psy.returnPressed.connect(self.collectData)
        self.lineEdit_KG.returnPressed.connect(self.collectData)
        self.lineEdit_A.returnPressed.connect(self.collectData)
        self.lineEdit_f.returnPressed.connect(self.collectData)
        # Simulate button pressed
        self.simButton.toggled.connect(self.simButtonPressed)

    #METODOS DE UI VISUALES

    def hide_order_one(self):
        self.filterType.setCurrentIndex(0)
        self.filterType.hide()
        self.label_T.hide()
        self.lineEdit_T.clear()
        self.lineEdit_T.hide()
        self.unitsDDown_T.setCurrentIndex(0)
        self.unitsDDown_T.hide()
        self.comboBox_KG.setCurrentIndex(0)
        self.comboBox_KG.hide()
        self.lineEdit_KG.clear()
        self.lineEdit_KG.hide()
        self.unitsDDown_KG.setCurrentIndex(0)
        self.unitsDDown_KG.hide()

        if self.simButton.isChecked():
            self.simButton.toggle()

    def show_order_one(self):
        self.filterType.show()
        self.label_T.show()
        self.lineEdit_T.show()
        self.unitsDDown_T.show()
        self.comboBox_KG.show()
        self.lineEdit_KG.show()
        self.unitsDDown_KG.show()

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
        self.comboBox_KG.setCurrentIndex(0)
        self.comboBox_KG.hide()
        self.lineEdit_KG.clear()
        self.lineEdit_KG.hide()
        self.unitsDDown_KG.setCurrentIndex(0)
        self.unitsDDown_KG.hide()

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
        self.comboBox_KG.show()
        self.lineEdit_KG.show()
        self.unitsDDown_KG.show()

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


    #METODOS DE UI LOGICOS

    def order_change(self):

        if self.filterOrder.currentIndex() == 1:
            self.hide_order_two()
            self.show_order_one()
            self.data["w"] = None
            self.data["psy"] = None

        elif self.filterOrder.currentIndex() == 2:
            self.hide_order_one()
            self.show_order_two()

        else:
            self.hide_order_one()
            self.hide_order_two()

    def kgChange(self):
        self.lineEdit_KG.clear()
        self.data["K"] = None

        if self.simButton.isChecked():
            self.simButton.setChecked(False)

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

    def simButtonPressed(self):

        if self.simButton.isChecked():
            bck.plotZerosPoles(self, bck.pasabajos(1,1,1))

        elif self.simButton.isChecked() is False:
            print("heyu")
            self.axes.clear()
            self.canvas.draw()


    def collectData(self):

        self.data["filterOrder"] = self.filterOrder.currentIndex()
        if self.data["filterOrder"] == 1:
            self.data["filterType"] = self.filterType.currentText()
            self.data["T"] = np.float(self.lineEdit_T.text())
        else:
            self.data["filterType"] = self.filterType2.currentText()
            self.data["w"] = np.float(self.lineEdit_w.text())
            self.data["psy"] = np.float(self.lineEdit_psy.text())
        self.data["inputType"] = self.inputType.currentText()
        self.data["plotType"] = self.plotType.currentText()
        if self.comboBox_KG.currentText() == "K":
            self.data["K"] = np.float(self.lineEdit_KG.text())
        else:
            g = np.float(self.lineEdit_KG.text())
            self.data["K"] = bck.G2K(g, self.data["filterOrder"],
                                     self.data["filterType"], self.data["w"], self.data["psy"])
        self.data["A"] = np.float(self.lineEdit_A.text())
        if self.inputType.currentText() == "Senoide":
            self.data["f"] = np.float(self.lineEdit_f.text())

        for key in self.data:
            print(self.data[key])

    def PlotGraph(self):
        if self.data["plotType"] == "Salida":
            bck.plotOutput(self, bck.filterHandler(self.data["plotType"], self.data["filterOrder"], self.data["K"],
                                                   self.data["w"], self.data["psy"]), self.data["inputType"],
                           self.data["A"], self.data["f"], self.data["t"])

        elif self.data["plotType"] == "Bode":
            bck.plotBode(self, bck.filterHandler(self.data["plotType"], self.data["filterOrder"], self.data["K"],
                                                   self.data["w"], self.data["psy"]))

        elif self.data["plotType"] == "Polos/Ceros":
            bck.plotZerosPoles(self, bck.filterHandler(self.data["plotType"], self.data["filterOrder"], self.data["K"],
                                                   self.data["w"], self.data["psy"]))