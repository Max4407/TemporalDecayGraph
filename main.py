from tdg import TDG
import time

graph = TDG()

if __name__ == "__main__": 
    graph.insert(fr = "FT9",to ="FP7",weights = [0.9,0.3,0.4,0.6,0.2])
    graph.insert("PL8","TR6",weights = [0.6,0.5,0.46,0.92,0.24])
    time.sleep(1)
    snap = graph.snapshot()
    graph.insert(fr = "FT9",to = "FP7",weights = [0.7,0.2,0.3,0.9,0.3])
    graph.insert(fr = "PL8",to = "TR6",weights = [0.3,0.52,0.34,0.76,0.42])
    snap2 = graph.snapshot() 
    time.sleep(1)
    snap3 = graph.snapshot()
    print(snap)
    print()
    print(snap2)
    print()
    print(snap3)