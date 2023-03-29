# Punto 1

# import numpy as np
# import matplotlib.pyplot as plt
# n = np.arange(0,101)
# y =  np.sin(np.pi*(0.12*n))
# y2 = np.cos((2*np.pi)*(0.03*n))
# s = y+y2
# t = y*y2

# plt.plot(y,label="Y")
# plt.plot(y2,label="Y2")
# plt.title("Figura 1")
# plt.legend()
# plt.show()

# plt.plot(s,label="s",color="red")
# plt.plot(t,label="t",color="green")
# plt.title("Figura 2")
# plt.legend()
# plt.show()



# Punto 2

import cv2                                      # importa la libreria llamada cv2
import numpy as np                              # importa la libreria llamada numpy de forma que se pueda llamar como np

bgr = np.zeros((300,300,3), dtype =np.uint8)    # Crea una matriz de ceros con 300 columnas, 300 filas y lo repite 3 veces
bgr2 = np.zeros((3,5,3),dtype =np.uint8)
#print(bgr2)    
bgr[:,:,:]=(255,0,100)                          # reemplaza el valor 0 de las filas1 al 255, las filas 2 se quedan igual en ceros y las filas 3 cambian a 100
# bgr nos da un valor que puede ser traducido como el codigo rgb de un color
print(bgr.shape)
print(bgr) 
cv2.imshow("BGR",bgr)                           # imgshow nos muestra un cuadro con el color, segun el codigo RGB que retorna bgr
cv2.waitKey(0)                                  # waitKey nos permite que la imagen con el color no se cierre inmediatamente despues de abierto
cv2.destroyAllWindows()                         # Esta permite que la imagen se cierre sin errores

# bgr2[:,:,:]=(255,0,100)                          # reemplaza el valor 0 de las filas1 al 255, las filas 2 se quedan igual en ceros y las filas 3 cambian a 100
# # bgr nos da un valor que puede ser traducido como el codigo rgb de un color
# cv2.imshow("BGR2",bgr2)                           # imgshow nos muestra un cuadro con el color, segun el codigo RGB que retorna bgr
# cv2.waitKey(0)  


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
# create()

# Por ahora me surguieron 2 errores ambos de sintaxis: 
# line 12, copie la V en minuscula y al correr el codigo me aparecia un error acerca del congelamiento del sistema 
# line 7, copie "-- version" separados y me aparecia que no encontraba la vesion de pip y por ente tambien se congelaba