import pandas as pd
import numpy as np

s = pd.Series(
    data=['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'zero', 10.10, 98],
    index=range(6, 26, 2))
s1 = pd.Series(
    data=['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'zero', 10.10, 98],
    index=range(2, 12))
# 1 ответ не может быть определен, так как складываются значения с разными типами данных

all_ints = []

for i in range(2, 12):
    if type(s1[i]) == int:
        all_ints.append(s1[i])

a = np.asarray(all_ints)

print(np.var(a , ddof=0), 'Ответ под пунктом 4')
