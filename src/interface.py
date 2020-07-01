# Qt Modules
from src.ui.mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import src.backend as bck

# Matplotlib Modules
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# Python Module
import numpy as np


class myWidget (QMainWindow, Ui_MainWindow):

    # INIT
    def __init__(self):
        super().__init__()

        # Initial setup
        self.setupUi(self)
        self.setWindowTitle("SIMBA")
        self.simButton.setCheckable(True)

        # User inputted data
        self.data = {
            "filterOrder": None,
            "filterType": None,
            "inputType": None,
            "plotType": None,
            "ampOrFase": None,
            "T": None,
            "w": None,
            "psy": None,
            "K": None,
            "A": None,
            "f": None
        }

        # Hide assets for first use
        self.hide_order_one()
        self.hide_order_two()
        self.hide_pulse_input()
        self.hide_sin_input()
        self.ampOrFase.hide()

        # Creates figure and canvas.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create toolbar
        toolbar = NavigationToolbar(self.canvas, self)

        plot_layout = QtWidgets.QVBoxLayout()
        plot_layout.addWidget(toolbar)
        plot_layout.addWidget(self.canvas)

        plot_widget = QtWidgets.QWidget()
        plot_widget.setLayout(plot_layout)

        # Sets current index in canvas to show plot.
        canvas_index = self.graphics.addWidget(plot_widget)
        self.graphics.setCurrentIndex(canvas_index)

        # Adds axes to figure.
        self.axes = self.figure.add_subplot()

        # Connections to callbacks

        # New filter order chosen
        self.filterOrder.currentIndexChanged.connect(self.orderChange)
        # Switched between K and G
        self.comboBox_KG.currentIndexChanged.connect(self.kgChange)
        # New input type chosen
        self.inputType.currentIndexChanged.connect(self.inputChange)
        # New plot type chosen
        self.plotType.currentIndexChanged.connect(self.plotChange)
        # Switch between Amp or Phase
        self.ampOrFase.currentIndexChanged.connect(self.switchBodePlot)
        # Intro pressed on data field
        self.lineEdit_T.returnPressed.connect(self.dataInput)
        self.lineEdit_w.returnPressed.connect(self.dataInput)
        self.lineEdit_psy.returnPressed.connect(self.dataInput)
        self.lineEdit_KG.returnPressed.connect(self.dataInput)
        self.lineEdit_A.returnPressed.connect(self.dataInput)
        self.lineEdit_f.returnPressed.connect(self.dataInput)
        # Simulate button pressed
        self.simButton.toggled.connect(self.simButtonPressed)

    # METODOS DE UI VISUALES

    # Esconde los metodos de input relacionados con filtros de primer orden
    def hide_order_one(self):
        self.filterType.setCurrentIndex(0)
        self.filterType.hide()
        self.label_T.hide()
        self.lineEdit_T.clear()
        self.lineEdit_T.hide()
        self.comboBox_KG.setCurrentIndex(0)
        self.comboBox_KG.hide()
        self.lineEdit_KG.clear()
        self.lineEdit_KG.hide()

        if self.simButton.isChecked():
            self.simButton.toggle()
    # Muestra los metodos de input relacionados con filtros de primer orden
    def show_order_one(self):
        self.filterType.show()
        self.label_T.show()
        self.lineEdit_T.show()
        self.comboBox_KG.show()
        self.lineEdit_KG.show()
    # Igual a las anteriores pero para orden dos
    def hide_order_two(self):
        self.filterType2.setCurrentIndex(0)
        self.filterType2.hide()
        self.label_w.hide()
        self.label_psy.hide()
        self.lineEdit_w.clear()
        self.lineEdit_w.hide()
        self.lineEdit_psy.clear()
        self.lineEdit_psy.hide()
        self.comboBox_KG.setCurrentIndex(0)
        self.comboBox_KG.hide()
        self.lineEdit_KG.clear()
        self.lineEdit_KG.hide()

        if self.simButton.isChecked():
            self.simButton.toggle()

    def show_order_two(self):
        self.filterType2.show()
        self.label_w.show()
        self.label_psy.show()
        self.lineEdit_w.show()
        self.lineEdit_psy.show()
        self.comboBox_KG.show()
        self.lineEdit_KG.show()

    def hide_pulse_input(self):
        self.label_A.hide()
        self.lineEdit_A.clear()
        self.lineEdit_A.hide()

        if self.simButton.isChecked():
            self.simButton.toggle()

    def show_pulse_input(self):
        self.label_A.show()
        self.lineEdit_A.show()

    def hide_sin_input(self):
        self.label_A.hide()
        self.label_f.hide()
        self.lineEdit_A.clear()
        self.lineEdit_A.hide()
        self.lineEdit_f.clear()
        self.lineEdit_f.hide()

        if self.simButton.isChecked():
            self.simButton.toggle()

    def show_sin_input(self):
        self.label_A.show()
        self.label_f.show()
        self.lineEdit_A.show()
        self.lineEdit_f.show()


    # METODOS DE UI LOGICOS

    # Maneja el cambio de orden del filtro
    def orderChange(self):

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
    # Maneja el cambio entre ingresar K o G
    def kgChange(self):
        self.lineEdit_KG.clear()
        self.data["K"] = None

        if self.simButton.isChecked():
            self.simButton.setChecked(False)
    # Maneja el cambio de entrada al sistema
    def inputChange(self):

        if self.inputType.currentIndex() == 1:
            self.hide_pulse_input()
            self.show_sin_input()

        elif self.inputType.currentIndex() == 2:
            self.hide_sin_input()
            self.show_pulse_input()

        else:
            self.hide_pulse_input()
            self.hide_sin_input()
    # Maneja el cambio de grafico deseado
    def plotChange(self):

        if self.plotType.currentText() == "Bode":
            self.ampOrFase.show()
        else:
            self.ampOrFase.hide()
    # Maneja la seleccion de tipo de grafico de Bode (amp/fase)
    def switchBodePlot(self):

        self.activateAwesomeness()
    # Maneja el evento de apretado del boton de simulacion (toggle)
    def simButtonPressed(self):

        self.activateAwesomeness()

        if self.simButton.isChecked() is False:
            self.axes.clear()
            self.canvas.draw()
    # Maneja el evento de ingreso de valores a partir de los lineEdits
    def dataInput(self):

        self.activateAwesomeness()
    # Si la simulacion esta activada, recolecta los datos necesarios y plotea en la ventana
    def activateAwesomeness(self):
        if self.simButton.isChecked():
            if self.collectData():
                self.plotGraph()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Faltan Datos!")
                msg.setText("Debe ingresar todos los parámetros para simular!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
    # Recolecta toda la informacion ingresada por el usuario y la valida en el proceso
    def collectData(self):
        allGHomie = True

        if self.filterOrder.currentIndex() != 0:
            self.data["filterOrder"] = self.filterOrder.currentIndex()
            if self.data["filterOrder"] == 1:
                if self.filterType.currentIndex() != 0:
                    self.data["filterType"] = self.filterType.currentText()
                else:
                    allGHomie = False
                if self.lineEdit_T.text() != "":
                    self.data["T"] = np.float(self.lineEdit_T.text())
                else:
                    allGHomie = False
            elif self.data["filterOrder"] == 2:
                if self.filterType2.currentIndex() != 0:
                    self.data["filterType"] = self.filterType2.currentText()
                else:
                    allGHomie = False
                if self.lineEdit_w.text() != "":
                    self.data["w"] = np.float(self.lineEdit_w.text())
                else:
                    allGHomie = False
                if self.lineEdit_psy.text() != "":
                    self.data["psy"] = np.float(self.lineEdit_psy.text())
                else:
                    allGHomie = False
            if self.plotType.currentIndex() != 0:
                self.data["plotType"] = self.plotType.currentText()
                if self.plotType.currentText() == "Bode":
                    self.data["ampOrFase"] = self.ampOrFase.currentText()
                else:
                    self.data["ampOrFase"] = None
            else:
                allGHomie = False
            if self.inputType.currentIndex() != 0:
                self.data["inputType"] = self.inputType.currentText()
                if self.lineEdit_A.text() != "":
                    self.data["A"] = np.float(self.lineEdit_A.text())
                else:
                    allGHomie = False
                if self.inputType.currentText() == "Senoide":
                    if self.lineEdit_f.text() != "":
                        self.data["f"] = np.float(self.lineEdit_f.text())
                    else:
                        allGHomie = False
            elif self.plotType.currentText() != "Bode" and self.plotType.currentText() != "Polos/Ceros":
                allGHomie = False
            if self.lineEdit_KG.text() != "":
                if self.comboBox_KG.currentText() == "K":
                    self.data["K"] = np.float(self.lineEdit_KG.text())
                elif self.comboBox_KG.currentText() == "G":
                    g = np.float(self.lineEdit_KG.text())
                    self.data["K"] = bck.G2K(g, self.data["filterOrder"],
                                             self.data["filterType"], self.data["w"],self.data["T"], self.data["psy"])
            else:
                allGHomie = False
        else:
            allGHomie = False

        if allGHomie == False:
            self.dumpData()

        return allGHomie
    # Se deshace de todos los valores recolectados para comenzar de nuevo
    def dumpData(self):

        for key in self.data:
            self.data[key] = None
    # Dibuja el grafico pedido en la ventana principal
    def plotGraph(self):
        if self.data["plotType"] == "Salida":
            bck.plotOutput(self, bck.filterHandler(self.data["filterType"], self.data["filterOrder"], self.data["K"],
                                                   self.data["w"], self.data["T"], self.data["psy"]), self.data["inputType"],
                           self.data["A"], self.data["f"])

        elif self.data["plotType"] == "Bode":
            if self.data["ampOrFase"] == "Amplitud":
                bck.plotBodeMag(self, bck.filterHandler(self.data["filterType"], self.data["filterOrder"], self.data["K"],
                                                   self.data["w"], self.data["T"], self.data["psy"]))
            elif self.data["ampOrFase"] == "Fase":
                bck.plotBodePhase(self,
                                bck.filterHandler(self.data["filterType"], self.data["filterOrder"], self.data["K"],
                                                  self.data["w"], self.data["T"], self.data["psy"]))


        elif self.data["plotType"] == "Polos/Ceros":
            bck.plotZerosPoles(self, bck.filterHandler(self.data["filterType"], self.data["filterOrder"], self.data["K"],
                                                   self.data["w"], self.data["T"], self.data["psy"]))