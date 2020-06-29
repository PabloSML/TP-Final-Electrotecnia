from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin

# #Filtro pasa bajos
# Orden 1:
#   H(s)=k/((s/wo)+1)
# Orden 2:
#   H(s)=k/((s/wo)^2+2*(s/wo)*e+1)
def pasabajos(orden,k,wo,e=0):
    if orden == 1:
        return signal.TransferFunction([k], [1/wo, 1])
    elif orden == 2:
        return signal.TransferFunction([k], [(1/wo)**2, 2*e/wo, 1])

# #Filtro pasa altos
# Orden 1:
#   H(s)=k*s/((s/wo)+1)
# Orden 2:
#   H(s)=k*s^2/((s/wo)^2+2*(s/wo)*e+1)
def pasaaltos(orden,k,wo,e=0):
    if orden == 1:
        return signal.TransferFunction([k,0], [1/wo, 1])
    elif orden == 2:
        return signal.TransferFunction([k,0,0], [(1/wo)**2, 2*e/wo, 1])

# #Filtro pasa todo
# Orden 1:
#   H(s)=k((s/wo)-1)/((s/wo)+1)
# Orden 2:
#   H(s)=k((s/wo)^2-2*(s/wo)*e+1)/((s/wo)^2+2*(s/wo)*e+1)
def pasatodo(orden,k,wo,e=0):
    if orden == 1:
        return signal.TransferFunction([k/wo,-k], [1/wo, 1])
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
def setgrids():
    plt.minorticks_on()
    plt.grid(which='major', color='black', linewidth=0.8, linestyle='--')
    plt.grid(which='minor', color='black', linewidth=0.4, linestyle=':')

#Respuesta a la entrada
#   Entrada: 'sin' o 'pulso'
#   t:intervalo de tiempo
#Devuelve la respuesta de salida
def respuesta(filtro,entrada,A, w, t):
    if entrada == 'sin':
        return signal.lsim(filtro,U=A*sin(w*t),T=t)
    elif entrada == 'pulso':
        return signal.lsim(filtro,U=[A for i in t],T=t)

#Plot de los ceros y polos de la funcion de transferencia.
#   sys: funcion de transferencia
#   pcolor: color de los polos.
#   zcolor: color de los ceros.
def plotZerosPoles(sys,pcolor='blue', zcolor ='red'):
    plt.figure()
    plt.axis('equal')
    sys2 = signal.TransferFunction([1, 0, -9], [1, -8, 17])
    # ax = plt.axes()
    # plot unit circle
    theta = np.linspace(-np.pi, np.pi, 201)
    plt.plot(np.sin(theta), np.cos(theta), color='gray', linewidth=0.2)
    # plot x-y axis
    plt.axhline(y=0, color='gray', linewidth=1)
    plt.axvline(x=0, color='gray', linewidth=1)
    plt.plot(np.real(sys.poles), np.imag(sys.poles), 'x', label='Poles', markersize=9, color='none',
             markeredgecolor= pcolor)
    plt.plot(np.real(sys.zeros), np.imag(sys.zeros), 'o', label='Zeros', markersize=9, color='none',
             markeredgecolor= zcolor)
    plt.minorticks_on()
    plt.legend()

