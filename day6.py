import numpy as np

f = open("day6.txt")
txt = f.read()

len(txt)

[i for i in txt[0:4]]
len({i for i in txt[0:4]})

for i in range(4, len(txt)):
    substring = txt[i-4:i]
    if len({i for i in txt[i-4:i]}) == 4:
        break
print(i)


for i in range(14, len(txt)):
    substring = txt[i-14:i]
    if len({i for i in txt[i-14:i]}) == 14:
        break
print(i)