import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2, 2.01, 0.01)
plt.plot(x, x**7 + np.tan(x))
plt.plot(x, x**6 + np.tan(x))
plt.show()