from edge import Edge
from typing import Dict, List

class TDG:
    def __init__(self): 
        self.edges : Dict[(str,str), Edge]= {} # edge list
        all_edges = ["A2-A1", "C3", "C4", "Cz", "F3", "F4", "F7", "F8", "Fp1", "Fp2", "Fz", 
                     "O1", "O2", "Oz", "P3", "P4", "Pz", "T3", "T4", "T5", "T6"]
        for i in range(0,len(all_edges) - 1):
            for j in range(i+1,len(all_edges)):
                self.edges[(all_edges[i],all_edges[j])] = Edge(all_edges[i],all_edges[j],[0,0,0,0,0])            
    
    def insert(self, source : str, target : str, weights : List[float]): #insert new edge, or update if it exists
        if source == target:
            raise NameError("must be two different electrodes")
        elif source < target:                #alphabetize electrodes so there are no dupes (ex: F7 - F8 and F8 to F7)
            newEdge = (source,target)
        else:
            newEdge = (target,source)
        if newEdge in self.edges:
            self.recalcWeight(newEdge[0], newEdge[1], weights)         #if edge already exists, recalculate weight with the new weight
            return newEdge
        else:
            raise NameError("edge does not exist")
        
    
    def recalcWeight(self, source: str, target: str, newWeights: List[float]):  
        recalcedEdge = self.edges.get((source,target))
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