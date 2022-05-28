from perlin_noise import PerlinNoise
import numpy as np
import matplotlib.pyplot as plt

shape = (50,50)
scale = 100.0
octaves = 8
seed = np.random.randint(232)
world = np.zeros(shape)

noise = PerlinNoise(octaves=octaves,
                   seed=seed)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise([i/scale, j/scale])
plt.imshow(world, cmap='terrain')
plt.show()