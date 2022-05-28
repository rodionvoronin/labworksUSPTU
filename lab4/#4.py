import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()

x = np.linspace(0, 2 * np.pi, 100)
(ln) = ax.plot(x, x**2 - np.cos(x), animated=False)
plt.show(block=False)
plt.pause(0.1)
bg = fig.canvas.copy_from_bbox(fig.bbox)
ax.draw_artist(ln)
fig.canvas.blit(fig.bbox)
j = 0
while True:
    fig.canvas.restore_region(bg)
    ln.set_ydata(np.sin(x + (j / 100) * np.pi))
    ax.draw_artist(ln)
    fig.canvas.blit(fig.bbox)
    fig.canvas.flush_events()
    plt.pause(.1)
    j += 1