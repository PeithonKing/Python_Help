import matplotlib as plt
import numpy as np
x = np.linspace(-10,10,100)
y = x**2
plt.plot(x,y)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
