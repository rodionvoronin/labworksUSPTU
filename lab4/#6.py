import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('https://query.data.world/s/bdu6cjyphtpfd5t4bpgz5zznrahtja')

x = df['Date'].values
y = df['Daily Confirmed'].values
fig = plt.figure(figsize=(25, 5))
ax = plt.gca()
plt.xticks(np.arange(35), labels=x, rotation=-90)
ax.xaxis.set_major_locator(plt.MaxNLocator(35))

plt.show()