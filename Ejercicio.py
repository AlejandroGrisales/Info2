import pandas as pd
import numpy as np
import os
import glob

# Punto 1
# Tomando el .csv compartido la clase anterior, cree un  nuevo  dataframe  
# donde  el  indice  0  del dataframe corresponda al sujeto de menor edad 
# y el  ultimo  indice  corresponda  al  sujeto  de  mayor edad.

mmse2 =  pd.read_csv(r"C:\Users\SALASDRAI\Desktop\clase\Info2\MMSE.csv",sep=";")

# print("-----------size-----------\n"+str(mmse2.size))
# print("\n-----------shape-----------\n"+str(mmse2.shape))
# print("\n-----------columnas-----------\n")
# print(mmse2.columns)
# print(mmse2["Edad en la visita"])

mmse2_copy=mmse2.copy()
mmse2_copy=mmse2_copy.set_index("Edad en la visita")
mmse2_copy=mmse2_copy.sort_index()
print("Punto 1\n")
print("\n------------------------------Dataframe Nuevo---------------------------\n")
print(mmse2_copy)

# Punto 2  
# Inserte  las  columnas  del  otro  archivo  entregado llamado 'EVALUACIONMEDICA.csv'

mmse3 =  pd.read_excel(r"C:\Users\SALASDRAI\Desktop\clase\Info2\EVALUACIONMEDICA.xlsx",sep=";")
# print("\n-----------size-----------\n"+str(mmse3.size))
# print("\n-----------shape-----------\n"+str(mmse3.shape))
# print("\n-----------columnasEVALUACIONMEDICA-----------\n")
# print(mmse3.columns)
mmse3_copy=mmse3.copy()
mmse2_copy=mmse2.copy()

mmse=mmse2_copy.merge(mmse3_copy, how='inner')
print("\nPunto 2\n")
print("\n------------------------------Dataframe Nuevo---------------------------\n")
print(mmse)


# Punto 3 
# Cuente el número de celdas que no son NaN para cada columna.

# Punto 4 
# Invierta el DataFrame, las filas serán las columnas.

# Punto 5  
# Tome  el  DataFrame  del  punto  2  y  reorganice  las columnas en orden alfabetico.
