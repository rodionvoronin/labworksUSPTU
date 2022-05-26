import pandas as pd
import numpy as np
import seaborn as sns

taxis = sns.load_dataset('taxis')
taxis.head()

# table = df.pivot_table(values='values',
                       #index='somecolumn',
                       #columns='somecolumn',
                       #aggfunc='mean',
                       #fill_value=0)

s = taxis.groupby(['pickup_zone', 'dropoff_zone'])['pickup'].mean()

print(s)