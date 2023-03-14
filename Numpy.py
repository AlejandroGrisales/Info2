import numpy as np
a= np.array([(1.5,2,3),(4,5,6)])
b= np.arange(15).reshape(3,5)

a.ndim          # El número de ejes (dimensiones) de la matriz.
a.shape         # El tamaño de lamatriz en cada dimensión.
a.size          # El número total de elementos de la matriz. 
a.itemsize      # El tamaño en bytes de cada elemento de la matriz.    
a.data          # El búfer que contiene los elementos reales de la matriz.
a.dtype.name    
c = np.array([[1, 2], [3, 4]], dtype=complex) # Ejemplo de dtype, pero no entiendo como funciona

np.array([1,2,3])   # Crea una matriz con las filas,columnas y datos que pogamos entre los parentesis
np.zeros(2)         # Crea una matirz con 2 ceros
np.ones(2)          # Crea una matriz con 2 unos
np.arange(4)        # Crea una matriz con los numeros del 0 al 3
np.arange(2,9,2)    # Crea una matriz del 2 al 8 con saltos de 2 numeros
np.empty(2)         # Crea una matriz con 2 elementos al azar
np.linspace(0,10, num=5)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)        #ordena los numeros de la matriz en orden ascendente


e = np.array([1, 2, 3, 4])
f = np.array([5, 6, 7, 8])
np.concatenate((a, b))

np.random.seed(0)
np.random.rand(3,2)     # Crea una matriz 3x2 con numeros aleatorios
rg = np.random.default_rng(1)
r=rg.random((3, 4))


g = np.array([[ 1.14022471,2.96360618],[ 3.37601032,4.25528411],[ 5.49313049,6.94909878]])
# Para matrices con numeros decimales
h = np.floor (g)        # Devuelve el valor entero redondeado hacia abajo
i = np.ceil (g)         # Devuelve el valor entero redondeado hacia arriba
j = np.round (g,3)      # Devuelve el valor con las cifras decimales especificadas

i.reshape(2, 3)         # Cambia la matriz, en este caso, de 3x2 a 2x3 sin cambiar el contenido
i.reshape(3, -1)        # Si se da una dimensión como -1en una operación de remodelación,las otras dimensiones se calculan automáticamente
k = i.T                 # devuelve la transpuesta de la matriz
