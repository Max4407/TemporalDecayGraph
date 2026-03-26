from typing import List
import time

class Edge:    
    def __init__(self, i, j, w = None): 
        self.source : str = i # source and target are the electrodes that the coherence is being measured between 
        self.target : str = j
        self.weights : List[float] = w # list of weights for the frequency bands Delta, Theta, Alpha, Beta, and Gamma
        self.last_computed : float = time.time() # time of last recalculation for the exponential decay
        
    def recalculate(self, newWeights = None): # handles exponential decay/factoring in new weights
        new_time = time.time()
        if self.weights == None:
            self.weights = newWeights
            return
        if newWeights == None:
            for i in range(0,len(self.weights)):
                self.weights[i] = (self.weights[i] * pow(0.5,time.time() - self.last_computed))
        else:
            for i in range(0,len(self.weights)):
                self.weights[i] = (0.5 * newWeights[i]) + (0.5 * (self.weights[i] * pow(0.5,time.time() - self.last_computed)))
        self.last_computed = new_time

    