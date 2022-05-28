import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100)
y = x**2 - x**5 + 1
plt.subplot(2, 2, 1)
plt.plot(x, y, 'r-', label='Функция 1')
y1 = x**3 + x**7
plt.subplot(2, 2, 3)
plt.plot(x, y1, 'b-', label='Функция 2')

plt.legend()
plt.show()