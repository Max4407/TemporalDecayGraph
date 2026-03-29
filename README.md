# TemporalDecayGraph
Temporal decay graph project to interact with an EEG and increase efficiency of real-time data processing and display, as well as Min-Heap Sliding Window for benchmarking.

Install required packages:

pip install matplotlib networkx numpy scipy pyedflib

Files

- `tdg.py` — Temporal Decay Graph implementation
- `edge.py` — Edge class used by TDG
- `mhsw.py` — Min-Heap Sliding Window implementation
- `visualizer.py` — Real-time EEG connectivity visualizer
- `main.py` — Entry point, runs the visualizer with sample data

To Run:
    Visualizer:
        ........
        

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
    

References:
    https://ifelldh.tec.mx/sites/g/files/vgjovo1101/files/Muse_2_Specifications.pdf
    https://www.epilepsy.com/diagnosis/eeg/how-read
    https://www.geeksforgeeks.org/python/python-visualize-graphs-generated-in-networkx-using-matplotlib/
    https://www.geeksforgeeks.org/python/regular-threads-vs-daemon-threads-in-python/
    https://networkx.org/documentation/stable/reference/
    https://matplotlib.org/stable/api/_as_gen/
    
