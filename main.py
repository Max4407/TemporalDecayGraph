from tdg import TDG
from visualizer import EEGVisualizer
import time
import threading


graph = TDG()
visuals = EEGVisualizer()

if __name__ == "__main__": 
    graph.insert("F3","F7",[0.9,0.3,0.4,0.6,0.2])
    graph.insert("F8","F4",[0.9,0.5,0.46,0.92,0.24])
    graph.insert("F3","F7",[0.7,0.2,0.3,0.9,0.3])
    graph.insert("F7","Fp1",[0.7,0.2,0.3,0.9,0.3])
    graph.insert("F3","Fp1",[0.7,0.2,0.3,0.9,0.3])
    graph.insert("F4","Fp2",[0.7,0.2,0.3,0.9,0.3])
    graph.insert("F8","Fp2",[0.7,0.2,0.3,0.9,0.3])
    graph.insert("F8","F4",[0.9,0.52,0.34,0.76,0.42])
    timebefore = time.time()
    
    def updateGraph():
        while True:
            snap = graph.snapshot()
            visuals.update(snap)
            time.sleep(0.1)

    t = threading.Thread(target=updateGraph, daemon=True)
    t.start()
    
    visuals.show()
    
    
