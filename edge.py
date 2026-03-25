from typing import List
import time

class Edge:    
    def __init__(self, i, j, w):
        self.source : str = i
        self.target : str = j
        self.weights : List[float] = w
        self.last_computed : float = time.time()
        
    def recalculate(self, newWeights = None): 
        new_time = time.time()
        if newWeights == None:
            for i in range(0,len(self.weights)):
                self.weights[i] = (self.weights[i] * pow(0.5,time.time() - self.last_computed))
        else:
            for i in range(0,len(self.weights)):
                self.weights[i] = (0.5 * newWeights[i]) + (0.5 * (self.weights[i] * pow(0.5,time.time() - self.last_computed)))
        self.last_computed = new_time

    