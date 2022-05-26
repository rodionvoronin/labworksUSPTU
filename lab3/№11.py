import pandas as pd
import numpy as np
import seaborn as sns

penguins = sns.load_dataset('penguins')
penguins.head()

print(penguins.groupby('sex')['body_mass_g'].agg([max, min]))

print(penguins[penguins['body_mass_g'] == 6300.0])
print(penguins[penguins['body_mass_g'] == 2700.0])