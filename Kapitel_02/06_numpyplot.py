import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y,"r--")
plt.plot(x,y2,"k--")
plt.axis("equal")
plt.title("Dies ist eine Sinuskurve")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
