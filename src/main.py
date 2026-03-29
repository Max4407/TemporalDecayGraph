from tdg import TDG
from mhsw import MHSW
from visualizer import EEGVisualizer
from csvparser import CSVParser
from config import DATA_HZ
import time
import threading

graph = TDG()
visuals = EEGVisualizer()
parser = CSVParser("TDG_trial_run_data_LONG.csv",190)
sleepTime = 1.0 / DATA_HZ

title = "baseline"

def updateVisuals():
    while True:
        snap = graph.snapshot()
        visuals.update(snap,title)
        time.sleep(sleepTime)

def streamData():
    global title
    window = parser.nextWindow();
    while window:
        title = window[0][3]
        for edge in window:
            graph.insert(edge[0],edge[1],edge[2])
        window = parser.nextWindow();
        time.sleep(sleepTime)
    visuals.close()

if __name__ == "__main__": 
    
    d = threading.Thread(target=streamData, daemon=True)
    d.start()
    
    v = threading.Thread(target=updateVisuals, daemon=True)
    v.start()
    
    visuals.show()   