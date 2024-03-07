#RPS_Training

#def update_Q(prev_play, current-play, outcome, Q):

import pandas as pd
import numpy as np
import random


def Q_update(prev_play,current_play,outcome,Q,alpha,gamma):     #Updating the Q-table
    #Change outcome to either 1 or -1
    Q[prev_play][current_play] = Q[prev_play][current_play]  + alpha*(outcome + gamma*max(Q[prev_play[-1] + current_play]) - Q[prev_play][current_play])
    return Q


def play_next(current_play,Q,epsilon):               #Function deciding which move to play
    if np.random.uniform(0,1) < epsilon:            #Randomnizer deciding if the optimal or random move should be played 
        action = random.choice(['R', 'P', 'S'])     #Pick random move
    else:
        action = Q[current_play].idxmax()           #Play the best move according to the Q-table
    return action, epsilon-0.0001