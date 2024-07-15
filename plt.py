#Gráficos

import matplotlib.pyplot as plt
import numpy as np

x =  np.linspace(0,5,100)
y = x**3
plt.plot(x,y)
plt.show()