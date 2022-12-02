import numpy as np
import pandas as pd

df = pd.read_csv('day2.txt', header=None, names=['col1', 'col2'], delimiter=" ")
df.shape

score = []
for i in range(df.shape[0]):
    play1 = df['col1'][i]
    play2 = df['col2'][i]

    play2 = play2.replace('X', 'A')
    play2 = play2.replace('Y', 'B')
    play2 = play2.replace('Z', 'C')

    if play2 == 'A':
        play2score = 1
    if play2 == 'B':
        play2score = 2
    if play2 == 'C':
        play2score = 3

    if play1 == play2:
        score.append(play2score + 3)

    if (play1 == 'A') & (play2 == 'B'):
        score.append(play2score + 6)
    if (play1 == 'A') & (play2 == 'C'):
        score.append(play2score + 0)

    if (play1 == 'B') & (play2 == 'A'):
        score.append(play2score + 0)
    if (play1 == 'B') & (play2 == 'C'):
        score.append(play2score + 6)
    
    if (play1 == 'C') & (play2 == 'A'):
        score.append(play2score + 6)
    if (play1 == 'C') & (play2 == 'B'):
        score.append(play2score + 0)

sum(score)

score = []
for i in range(df.shape[0]):
    play1 = df['col1'][i]
    play2 = df['col2'][i]

    #draw
    if play2 == 'Y':
        play2 = play1

    #lose
    if play2 == 'X':
        if play1 == 'A':
            play2 = 'C'
        if play1 == 'B':
            play2 = 'A'
        if play1 == 'C':
            play2 = 'B'
    #win
    if play2 == 'Z':
        if play1 == 'A':
            play2 = 'B'
        if play1 == 'B':
            play2 = 'C'
        if play1 == 'C':
            play2 = 'A'

    if play2 == 'A':
        play2score = 1
    if play2 == 'B':
        play2score = 2
    if play2 == 'C':
        play2score = 3

    if play1 == play2:
        score.append(play2score + 3)

    if (play1 == 'A') & (play2 == 'B'):
        score.append(play2score + 6)
    if (play1 == 'A') & (play2 == 'C'):
        score.append(play2score + 0)

    if (play1 == 'B') & (play2 == 'A'):
        score.append(play2score + 0)
    if (play1 == 'B') & (play2 == 'C'):
        score.append(play2score + 6)
    
    if (play1 == 'C') & (play2 == 'A'):
        score.append(play2score + 6)
    if (play1 == 'C') & (play2 == 'B'):
        score.append(play2score + 0)

sum(score)