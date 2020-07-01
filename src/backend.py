from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin

# #Filtro pasa bajos
# Orden 1:
#   H(s)=k/((s/T)+1)
# Orden 2:
#   H(s)=k/((s/wo)^2+2*(s/wo)*e+1)
def pasabajos(orden,k,wo,T,e):
    if orden == 1:
        return signal.TransferFunction([k], [1/T, 1])
    elif orden == 2:
        return signal.TransferFunction([k], [(1/wo)**2, 2*e/wo, 1])

# #Filtro pasa altos
# Orden 1:
#   H(s)=k*s/((s/T)+1)
# Orden 2:
#   H(s)=k*s^2/((s/wo)^2+2*(s/wo)*e+1)
def pasaaltos(orden,k,wo,T,e):
    if orden == 1:
        return signal.TransferFunction([k,0], [1/T, 1])
    elif orden == 2:
        return signal.TransferFunction([k,0,0], [(1/wo)**2, 2*e/wo, 1])

# #Filtro pasa todo
# Orden 1:
#   H(s)=k((s/T)-1)/((s/T)+1)
# Orden 2:
#   H(s)=k((s/wo)^2-2*(s/wo)*e+1)/((s/wo)^2+2*(s/wo)*e+1)
def pasatodo(orden,k,wo,T,e):
    if orden == 1:
        return signal.TransferFunction([k/T,-k], [1/T, 1])
    elif orden == 2:
        return signal.TransferFunction([k/(wo**2),-2*k*e/wo,k], [(1/wo)**2, 2*e/wo, 1])

#Filtro pasa banda
#   H(s)= ks/((s/wo)^2+2*(s/wo)*e+1)
def pasabanda(k,wo,e):
    return signal.TransferFunction([k,0],[(1/wo)**2, 2*e/wo, 1])

#Notch
#   H(s)= k((s/wo)^2+1)/((s/wo)^2+2*(s/wo)*e+1)
def notch(k,wo,e):
    return signal.TransferFunction([k/(wo**2), 0,1], [(1 / wo) ** 2, 2 * e / wo, 1])

# Set grids
def setgrids(self_axes):
    self_axes.minorticks_on()
    self_axes.grid(which='major', color='black', linewidth=0.8, linestyle='--')
    self_axes.grid(which='minor', color='black', linewidth=0.4, linestyle=':')

#Respuesta a la entrada
#   Entrada: 'Senoide' o 'Pulso'
#   t:intervalo de tiempo
#Devuelve la respuesta de salida
def respuesta(self,filtro,entrada,A, f):
    if entrada == 'Senoide':
        t=np.linspace(0,(500/f),num=100000)
        return signal.lsim(filtro,U=A*sin(2*np.pi*f*t),T=t)
    elif entrada == 'Pulso':
        if self.data["filterOrder"] == 1:
            t = np.linspace(0, (10000/self.data["T"]), num=100000)
        elif self.data["filterOrder"] ==2:
            t = np.linspace(0, (10000/self.data["w"]), num=100000)
        #t = np.linspace(0, 10, num=100000)
        return signal.lsim(filtro,U=[A for i in t],T=t)

#Plot de los ceros y polos de la funcion de transferencia.
#   sys: funcion de transferencia
#   pcolor: color de los polos.
#   zcolor: color de los ceros.
def plotZerosPoles(self, sys, pcolor='blue', zcolor='red'):
    # self.figure.delaxes(self.axes)
    # self.axes = self.figure.add_subplot(1, 1, 1)
    self.axes.clear()
    self.axes.axis('equal')
    sys2 = signal.TransferFunction([1, 0, -9], [1, -8, 17])
    # plot unit circle
    theta = np.linspace(-np.pi, np.pi, 201)
    self.axes.plot(np.sin(theta), np.cos(theta), color='gray', linewidth=0.2)
    # plot x-y axis
    self.axes.axhline(y=0, color='gray', linewidth=1)
    self.axes.axvline(x=0, color='gray', linewidth=1)
    self.axes.plot(np.real(sys.poles), np.imag(sys.poles), 'x', label='Poles', markersize=9, color='none',
                   markeredgecolor=pcolor)
    self.axes.plot(np.real(sys.zeros), np.imag(sys.zeros), 'o', label='Zeros', markersize=9, color='none',
                   markeredgecolor=zcolor)
    self.axes.minorticks_on()
    self.axes.legend()
    self.canvas.draw()

#Plot del diagrama de Bode
def plotBodeMag(self,sys):
    self.axes.clear()
    w, mag, phase = signal.bode(sys)
    self.axes.semilogx(w/(2*np.pi), mag)    # Bode magnitude plot
    self.axes.set_xlabel('Frecuencia (Hz)')
    self.axes.set_ylabel('Amplitud (dB)')
    setgrids(self.axes)
    self.canvas.draw()

#Plot diagrama de fase de Bode
def plotBodePhase(self,sys):
    self.axes.clear()
    w, mag, phase = signal.bode(sys)
    self.axes.semilogx(w / (2 * np.pi), phase)  # Bode phase plot
    self.axes.set_xlabel('Frecuencia (Hz)')
    self.axes.set_ylabel('Fase (°)')
    setgrids(self.axes)
    self.canvas.draw()


#Plot de la respuesta a la entrada
#   inputtype: 'sin' o 'pulso'
#   t:intervalo de tiempo
#Devuelve la respuesta de salida
def plotOutput(self,sys,inputtype,A,f):
    # self.figure.delaxes(self.axes)
    # self.axes = self.figure.add_subplot(1, 1, 1)
    self.axes.clear()
    output=respuesta(self,sys,inputtype,A,f)
    #Plot input
    if inputtype == 'Senoide':
        t=np.linspace(0,(500/f),num=100000)
        self.axes.plot(t,A*sin(2*np.pi*f*t),label="Entrada")
    elif inputtype == 'Pulso':
        t = np.linspace(0, 10, num=100000)
        self.axes.plot(t,[A for i in t],label="Entrada")
    #Plot output
    self.axes.plot(output[0],output[1],label= "Salida")
    self.axes.set_xlabel('Tiempo (s)')
    self.axes.set_ylabel('Amplitud'
    if inputtype == "Senoide":
        self.axes.set_xlim(0,(5/f))
    elif inputtype == "Pulso":
        if self.data["filterOrder"] ==1:
            self.axes.set_xlim(0, (100/self.data["T"]))
        elif self.data["filterOrder"] ==2:
            self.axes.set_xlim(0, (100/self.data["w"]))
    setgrids(self.axes)
    self.axes.minorticks_on()
    self.axes.legend()
    self.canvas.draw()

#Conversion de G a K segun orden y tipo de filtro
#   orden: 1,2
#   filtertype: "Pasa Bajos","Pasa Altos", "Pasa Todo", "Pasa Banda", "Notch"
def G2K(G,orden,filtertype,w,T,e):
    if filtertype=='Pasa Bajos' or filtertype=='Pasa Todo' or filtertype=='Notch' :
        return G
    if filtertype=='Pasa Altos':
        if orden ==1:
            return G*(1/T)
        elif orden ==2:
            return G*(1/w)**2
    if filtertype=='Pasa Banda':
        return G*2*e/w

#Devuelve la funcion de transferencia dependiendo del filtro
def filterHandler(filtro,orden,k,w,T,e):
    if filtro == "Pasa Bajos":
        return pasabajos(orden,k,w,T,e)
    elif filtro == "Pasa Altos":
        return pasaaltos(orden,k,w,T,e)
    elif filtro == "Pasa Todo":
        return pasatodo(orden,k,w,T,e)
    elif filtro == "Pasa Banda":
        return pasabanda(k,w,e)
    elif filtro == "Notch":
        return notch(k,w,e)