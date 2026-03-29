# EEG Dashboard
EEG dashboard project to display coherence data between EEG electrodes. Implemented using min heap and graph data structures to compare speeds and memory efficiencies with the goal of picking the fastest data structure for real-time processing and visualization. We found the graph to be more efficient because of the lower snapshot latency, which is what is used for the visualizer. This way, if the update speed of the visualizer is increased, the snapshots will be quick enough that there is minimal lag and delay. The min heap's advantage is that it stores all the data, whereas the graph updates the data but stores a fixed number of points. This means that the insertion time with smaller data sets will be much faster for the min heap.

<img width="2261" height="1239" alt="image" src="https://github.com/user-attachments/assets/780c4a51-8fbd-4d7e-8d09-893193c39fb5" />


Install required packages:

pip install matplotlib networkx 

Packages for data pipeline (not required to run the program):
numpy scipy pyedflib

Files

- `tdg.py` — Temporal Decay Graph implementation
- `edge.py` — Edge class used by TDG
- `mhsw.py` — Min-Heap Sliding Window implementation
- `visualizer.py` — Real-time EEG connectivity visualizer
- `main.py` — Entry point, runs the visualizer with sample data

To Run:
- make sure all src files are in same directory and the data csv file is in the parent directory (like in this repo)
- enter 'python main.py' in terminal

        

    Part of a real time BCI pipeline:
        TDG:
        ```python
        from tdg import TDG
        graph = TDG()
        graph.insert("F3", "F7", [0.9, 0.3, 0.4, 0.6, 0.2])  # source, target, [delta, theta, alpha, beta, gamma]
        snapshot = graph.snapshot()
        ```
        
        MHSW:
        ```python
        from mhsw import MHSW
        window = MHSW(window=5.0)  # retain data for 5 seconds
        window.insert("F3", "F7", [0.9, 0.3, 0.4, 0.6, 0.2])
        snapshot = window.snapshot()
        ```

        Both structures return a `Dict[(str, str), List[float]]` mapping electrode pairs 
        to a list of five coherence values: [delta, theta, alpha, beta, gamma].
    

References used while making visualizer:
    https://ifelldh.tec.mx/sites/g/files/vgjovo1101/files/Muse_2_Specifications.pdf
    https://www.epilepsy.com/diagnosis/eeg/how-read
    https://www.geeksforgeeks.org/python/python-visualize-graphs-generated-in-networkx-using-matplotlib/
    https://www.geeksforgeeks.org/python/regular-threads-vs-daemon-threads-in-python/
    https://networkx.org/documentation/stable/reference/
    https://matplotlib.org/stable/api/_as_gen/
    
