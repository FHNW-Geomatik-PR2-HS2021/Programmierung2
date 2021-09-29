import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

axes = plt.axes()

circle = patches.Circle((0,0), radius=1.0, fc=(1,0,0), ec=(0,0,0), lw=5)
circle2 = patches.Circle((5,0), radius=0.5, fc=(0,0,1), ec=(0,0,0), lw=2)

axes.add_patch(circle)
axes.add_patch(circle2)
plt.axis("equal")
plt.plot()
plt.show()