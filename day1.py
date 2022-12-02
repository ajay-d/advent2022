import numpy as np
import pandas as pd

df = pd.read_csv('day1.txt', header=None, names=['cal'], skip_blank_lines=False)

l = []
df.shape
cnt = 0
for i in range(df.shape[0]):
    if pd.isna(df['cal'][i]):
        l.append(cnt)
        cnt = 0
        continue
    cnt = cnt + df['cal'][i]

len(l)
max(l)

l.sort(reverse=True)
sum(l[0:3])