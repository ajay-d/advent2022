import numpy as np
import pandas as pd
import re
from collections import deque

x = pd.read_fwf('day5.txt', header=None, nrows=8, widths = [4, 4, 4, 4, 4, 4, 4, 4, 4])
allMoves = pd.read_csv('day5.txt', header=None, skiprows=9)

stacks = []
for i in range(9):
    stacks.append(x[i].dropna().astype('str'))
stacks = [list(i) for i in stacks]
[len(row) for row in stacks]
len([num for row in stacks for num in row])

[i[0] for i in stacks]
#stacks = [deque(i) for i in stacks]

#move = stacks[8][0:3]
#stacks[5] = stacks[5] + move
#stacks[5]

# for i in range(2):
#     curMove = allMoves[0][i]
#     _, n, _, src, _, dest = curMove.split(" ")
#     move = stacks[int(src)-1][0:int(n)]
#     move.reverse()
#     for j in range(int(n)):
#         stacks[int(src)-1].pop(0)
#     stacks[int(dest)-1] = move + stacks[int(dest)-1]
# stacks

for i in range(allMoves.shape[0]):
    curMove = allMoves[0][i]
    _, n, _, src, _, dest = curMove.split(" ")
    move = stacks[int(src)-1][0:int(n)]
    move.reverse()
    for j in range(int(n)):
        stacks[int(src)-1].pop(0)
    stacks[int(dest)-1] = move + stacks[int(dest)-1]
stacks
#check, total blocks must be same
len([num for row in stacks for num in row])
[i[0] for i in stacks]


move = stacks[8][0:3]
move + stacks[3]
stacks[3] = move + stacks[3]

for i in range(allMoves.shape[0]):
    curMove = allMoves[0][i]
    _, n, _, src, _, dest = curMove.split(" ")
    move = stacks[int(src)-1][0:int(n)]
    for j in range(int(n)):
        stacks[int(src)-1].pop(0)
    stacks[int(dest)-1] = move + stacks[int(dest)-1]
stacks

[i[0] for i in stacks]