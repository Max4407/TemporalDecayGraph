from edge import Edge
from typing import Dict, List

class TDG:
    def __init__(self): 
        self.edges : Dict[(str,str), Edge]= {} # edge lists
    
    def insert(self, fr : str, to : str, weights : List[float]):
        if fr == to:
            raise NameError("must be two different electrodes")
        elif fr < to:
            newEdge = (fr,to)
        else:
            newEdge = (to,fr)
        if newEdge in self.edges:
            self.recalcWeight(newEdge[0], newEdge[1], weights) 
        else:
            self.edges[newEdge] = Edge(newEdge[0],newEdge[1],weights)
        return newEdge
    
    def recalcWeight(self, fr: str, to: str, newWeights: List[float]):
        recalcedEdge = self.edges.get((fr,to))
        if recalcedEdge != None:
            recalcedEdge.recalculate(newWeights)
        return recalcedEdge
    
    def snapshot(self):
        state : Dict[(str, str), List[float]] = {}
        for i in self.edges:
            tempEdge = self.edges.get(i)
            tempEdge.recalculate()
            state[(i[0],i[1])] = list(tempEdge.weights)
        return state