# Realizar los ejercicios de la presentación 2.1 Numpy y subirlos en un .ipynb o al GitHub
import numpy as np
# Ejercicio 1

# Crear una matriz de ceros de tipo entero 3x4.
a = np.zeros(12).reshape(3,4)
print("Ejercicio 1.1")
print (a)
print (a.shape)

# Crear una matriz de ceros de tipo entero 3x4 exceptola primera fila que será uno.
a = np.zeros(8)
b = np.ones(4)
r = np.concatenate((b,a))
f = r.reshape(3,4)
print("\nEjercicio 1.2")
print(f)
print (f.shape)

# Crear una matriz de ceros de tipo entero 3x4 exceptola última fila que será el rango entre 5 y 8.
a = np.zeros(8)
b = np.arange(5,9)
r = np.concatenate((a,b))
f = r.reshape(3,4)
print("\nEjercicio 1.3")
print(f)
print (f.shape)

# Ejercicio 2

# Crea un vector de 10 elementos, siendo los índices impares unos y los índices pares dos.
a= np.array([1,2,1,2,1,2,1,2,1,2])
print("\nEjercicio 2.1")
print(a)
print (a.shape)

# Crea un «tablero de ajedrez», con unos en las casillas negras y ceros en las blancas.
a = np.array([0,1,0,1,0,1,0,1])
b = np.array([1,0,1,0,1,0,1,0])

c = np.concatenate((a,b))
d = np.concatenate((a,b))

g = np.concatenate((c,d))
h = np.concatenate((c,d))

i = np.concatenate((g,h))
j = i.reshape(8,8)

print("\nEjercicio 2.2")
print(j)
print (j.shape)

# Ejercicio 3

# Crea  una  matriz  aleatoria  5x5  y  halla  los  valores mínimo y máximo.
rg = np.random.default_rng(3)
r=rg.random((5, 5))
a = np.floor((10 *r))
print("\nEjercicio 3.1")
print(a)
print ("shape: "+str(a.shape))
print ("MIN: "+str(np.min(a)))
print ("MAX: "+str(np.max(a)))


# Normalizar la matriz anterior
b = a/np.linalg.norm(a)
print("\nEjercicio 3.1")
print(b)
