import os
from os import system

# nombre_env = input("Ingrese el nombre del entorno: ")
def create():
    system("Python -m pip install --upgrade pip")
    system("Python -m pip --version")
#     system("Python -m pip install --user virtualenv")
#     current= os.getcwd()
#     system("Python -m venv"+ current+"/"+str(nombre_env))
#    system(current+"/"+str(nombre_env)+"/"+"Scripts/activate")
    system("Python -V")
    system("Python -m pip install numpy")
    system("Python -m pip install matplotlib")
    system("Python -m pip install pandas")
    system("Python -m pip install scipy")
    system("Python -m pip install openxv-python")
    system("Python -m pip install mne")
    system("Python -m pip install Seaborn")
    system("Python -m pip install pingouin")
    print("Su entorno esta listo para ser utilizado")
# # create()

# Por ahora me surguieron 2 errores: 
# linea 12, copie la V en minuscula y al correr el codigo me aparecia un error acerca del congelamiento del sistema 
# linea 7, copie "-- version" separados y me aparecia que no encontraba la vesion de pip y por ente tambien se congelaba


# Punto 1
# Graficar en la misma figura las señales y[n] y y2[n], utilice leyenda y coloresdiferentes para cada señal. Asigne título a cada eje.
# Graficar en la misma figura las señales s[n] y t[n], utilice leyenda y coloresdiferentes para cada señal. Asigne título a cada eje.
import numpy as np
import matplotlib.pyplot as plt
n = np.arange(0,101)
y =  np.sin(np.pi*(0.12*n))
y2 = np.cos((2*np.pi)*(0.03*n))
s = y+y2
t = y*y2

plt.plot(y,label="Y")
plt.plot(y2,label="Y2")
plt.title("Figura 1")
plt.legend()
plt.show()

plt.plot(s,label="s",color="red")
plt.plot(t,label="t",color="green")
plt.title("Figura 2")
plt.legend()
plt.show()



# Punto 2
# Ejecute el siguiente codigo ydescriva que hace cada linea
import cv2                                      # importa la libreria llamada cv2
import numpy as np                              # importa la libreria llamada numpy de forma que se pueda llamar como np

bgr = np.zeros((300,300,3), dtype =np.uint8)    # Crea una matriz de ceros con 300 columnas, 300 filas y lo repite 3 veces
bgr[:,:,:]=(255,0,100)                          # reemplaza el valor 0 de las filas1 al 255, las filas 2 se quedan igual en ceros y las filas 3 cambian a 100
# bgr nos da un valor que puede ser traducido como el codigo rgb de un color
cv2.imshow("BGR",bgr)                           # imgshow nos muestra un cuadro de titulo BGR con el color, segun el codigo RGB que retorna bgr
cv2.waitKey(0)                                  # waitKey nos permite que la imagen con el color no se cierre inmediatamente despues de abierto
cv2.destroyAllWindows()                         # Esta permite que la imagen se cierre sin errores


# Punto 3
#Busque  un  metodo  que  permita  optimizar  la  toma  de  canales  de  una imagen y el metodo que permita reconstruir la imagen original a partir de los tres canales
#Tomar los 3 canales

import numpy as np
import cv2

#Leer la imagen
path = r"C:\Users\Alejo\Desktop\vs intentos\imagen.jpg"
img=cv2.imread(path)

imgR=img[:,:,0]
imgG=img[:,:,1]
imgB=img[:,:,2]

cv2.imwrite('ImagenX.png',imgR)

cv2.namedWindow('Ventana',0)
cv2.namedWindow('VentanaB',0)
cv2.namedWindow('VentanaG',0)
cv2.namedWindow('VentanaR',0)

cv2.imshow('Ventana',img)
cv2.imshow('VentanaR',imgB)
cv2.imshow('VentanaG',imgG)
cv2.imshow('VentanaB',imgR)

cv2.waitKey(0)
cv2.destroyAllWindows()