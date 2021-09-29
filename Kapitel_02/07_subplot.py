import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
y2 = np.cos(x)

plt.subplot(2,1,1)
plt.title("Dies ist eine Sinuskurve")
plt.plot(x,y,"r--")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(2,1,2)
plt.plot(x,y2,"k--")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
