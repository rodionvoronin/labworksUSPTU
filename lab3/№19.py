import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://query.data.world/s/yzxflf5flh3bis6q2glsqhaoaxzcce')

df = df.set_index('Date')
data1 = df['High']
data2 = df['Low']
data = [data1, data2]

plt.boxplot(data)

plt.show()

# верные высказывания: 1, 3, 5