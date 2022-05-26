import pandas as pd
import numpy as np
import seaborn as sns
import openpyxl

planets = sns.load_dataset('planets')
planets.head()

tp = planets[planets['method'] == 'Transit'] #все планеты, обнаруженные транзитным методом

s = tp.groupby('method')['mass'].max()

s.to_excel("output.xlsx")



