#pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Ejemplo 1
x = np.linspace(0,2*np.pi,200)
y = np.sin(x)

fig, ax= plt.subplots()
ax.plot(x,y)
plt.show()

#Ejemplo 2
fig = plt.figure()
fig, ax = plt.subplots()
ax.plot([1,2,3,4],[1,4,2,3])
plt.show()

#Ejemplo 3
fig, ax1, ax2 = plt.subplots()
ax1.plot([1,2,3,4],[1,4,2,3])
ax2.plot([1,2,2,4],[1,1,2,2])
ax.set_ylabel("Amplitud")
ax.set_xlabel("Tiempo")
plt.show()

#Ejemplo 4
plt.plot([0,2,0,4],[1,1,2,3])
plt.ylabel("Amplitud")
plt.xlabel("Tiempo")
plt.grid()

#Ejemplo 5
np.random.seed(19680801)
data = {"a":np.arange(50),
        "c":np.random.randint(0, 50, 50),
        "d":np.random.randn(50)}
data["b"] = data["a"] + 10*np.random.randn(50)
data["d"] = np.abs(data["d"])*100
fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
ax.scatter("a","b",c="c",s="d", data= data)
ax.set_xlabel("entry a")
ax.set_ylabel("entry b")
# plt.show()

#Ejemplo 6
plt.plot(np.random.rand(10),np.random.rand(10),color = "r",linestyle="--",linewidth=3, label="linea 2")
plt.plot(np.random.rand(10),np.random.rand(10),color = "b", label="linea 2")
plt.scatter(np.random.rand(10),np.random.rand(10),color = "g",edgecolor="b", label="puntos")
plt.ylabel("Amplitud")
plt.xlabel("Tiempo")
plt.grid()
plt.legend()


