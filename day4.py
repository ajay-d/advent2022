import numpy as np
import pandas as pd
import string

x = np.loadtxt('day4.txt', dtype=(np.dtype(str)))
sub = 0
for i in range(len(x)):
    pair = x[i]
    a,b = pair.split(',')
    a_split = a.split("-")
    b_split = b.split("-")
    a_list = set(range(int(a_split[0]), int(a_split[1])+1))
    b_list = set(range(int(b_split[0]), int(b_split[1])+1))
    if a_list.issubset(b_list) or b_list.issubset(a_list):
        sub += 1

overlap = 0
for i in range(len(x)):
    pair = x[i]
    a,b = pair.split(',')
    a_split = a.split("-")
    b_split = b.split("-")
    a_list = set(range(int(a_split[0]), int(a_split[1])+1))
    b_list = set(range(int(b_split[0]), int(b_split[1])+1))
    if a_list.intersection(b_list):
        overlap += 1