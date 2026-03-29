from typing import List
import time
from config import DECAY_RATE, PRUNING_CUTOFF

class Edge:    
    def __init__(self, i, j, w): 
        self.source : str = i # source and target are the electrodes that the coherence is being measured between 
        self.target : str = j
        self.weights : List[float] = w # list of weights for the frequency bands Delta, Theta, Alpha, Beta, and Gamma
        self.last_computed : float = time.time() # time of last recalculation for the exponential decay
        
    def recalculate(self, newWeights = None): # handles exponential decay/factoring in new weights
        new_time = time.time()
        if newWeights == None:
            for i in range(0,len(self.weights)):
                self.weights[i] = (self.weights[i] * pow(DECAY_RATE,time.time() - self.last_computed))
                if self.weights[i] < PRUNING_CUTOFF:
                    self.weights[i] = 0
        else:
            for i in range(0,len(self.weights)):
                if self.weights[i] == 0:
                    self.weights[i] = newWeights[i]
                else:
                    self.weights[i] = (0.5 * newWeights[i]) + (DECAY_RATE * (self.weights[i] * pow(0.5,time.time() - self.last_computed)))
                if self.weights[i] < PRUNING_CUTOFF:
                    self.weights[i] = 0

        self.last_computed = new_time

    