import matplotlib.pyplot as plt
import numpy as np
import random

N = 1000

x = np.random.randint(-100, 100, N)
y = np.random.randint(-100, 100, N)
color = np.random.random(size=(1,1000))

fig1 = plt.figure()
ax = fig1.add_subplot(1, 1, 1)
ax.scatter(x,y, c=color)
ax.set_title("Random colors", fontsize=14)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)
fig1.savefig("fig1.png")


# Aufgabe 2

def f(x,y):
    return np.exp(-x**2) * np.sin(y)

N = 1000
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.pcolormesh(X, Y, f(X, Y), cmap="viridis")
ax2.set_aspect("equal")
ax2.set_title("Exponentialfunktion", fontsize=14)
ax2.set_xlabel("X", fontsize=14)
ax2.set_ylabel("Y", fontsize=14)
fig2.savefig("fig2.png")

# Show all Plots
plt.show()