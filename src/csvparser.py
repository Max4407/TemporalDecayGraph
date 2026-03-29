from typing import List
from pathlib import Path

class CSVParser:
    def __init__(self, targetFile,windowSize): 
        pathtofile = Path(__file__).parent / '..' / targetFile
        self.file = open(pathtofile,"r")
        self.file.readline()
        self.window = windowSize

    def nextWindow(self):
        window = []
        for i in range (0,self.window):
            line = self.file.readline()
            if line:
                line = line.strip().split(",")
            else: return None
            title = line[3]
            source = line[4].split(" ")[1]
            target = line[5].split(" ")[1]
            delta = float(line[6])
            theta = float(line[7])
            alpha = float(line[8])
            beta = float(line[9])
            gamma = float(line[10])
            window.append([source,target,[delta,theta,alpha,beta,gamma],title])
        return window