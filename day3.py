import numpy as np
import pandas as pd
import string

x = np.loadtxt('day3.txt', dtype=(np.dtype(str)))

len(x)
len(x[0])

x[0]
list(x[0])
len(x[0])

intersect = []
for i in range(x.shape[0]):
    mid = np.int8(len(x[i])/2)
    a = x[i][0:mid]
    b = x[i][mid:]

    a = set(x[i][:mid])
    b = set(x[i][mid:])
    intersect.append(list(a.intersection(b))[0])

string.ascii_lowercase
string.ascii_uppercase
len(string.ascii_letters)
d = dict.fromkeys(string.ascii_letters, 0)
d = dict(zip(string.ascii_letters, list(range(1, 53))))
table = str.maketrans(d)

sum([d[i] for i in intersect])

l = [''] * 100
for i in range(x.shape[0]):
    idx = i//3
    l[idx] = l[idx] + " " + x[i]

intersect = []
for i in range(len(l)):
    a,b,c = l[i].split()
    inter = set(a).intersection(set(b)).intersection(set(c))
    intersect.append(list(inter)[0])
sum([d[i] for i in intersect])