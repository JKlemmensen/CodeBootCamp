import numpy as np

def calculate(input):
    y = np.reshape(input,(3,3))
    x = {'mean': [np.mean(y,axis=0), np.mean(y,axis=1),np.mean(y)],
         'variance': [np.var(y,axis=0), np.var(y,axis=1), np.var(y)],
         'standard deviation':  [np.std(y,axis=0), np.std(y,axis=1), np.std(y)],
         'max': [np.max(y,axis=0), np.max(y,axis=1), np.max(y)],
         'min': [np.min(y,axis=0), np.min(y,axis=1), np.min(y)],
         'sum': [np.sum(y,axis=0), np.sum(y,axis=1), np.sum(y)],
         }
    return x
