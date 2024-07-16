#Gráficos

import matplotlib.pyplot as plt
import numpy as np

x =  np.linspace(0,5,100)
y = x**3
plt.plot(x,y,"r--",label = "$x^3$", linewidth = 5)
plt.title("f(x) = x^3")
plt.legend()
plt.grid()
plt.show()
