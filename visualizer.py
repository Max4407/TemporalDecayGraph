import matplotlib.pyplot as mpl
import matplotlib.animation as ani
import networkx as nx 

class EEGVisualizer: 
    def __init__(self):
        self.positions = {                 #positions for electrodes on head diagram 
            "Fp1": (-0.18, 0.92), "Fpz": (0.00, 0.95), "Fp2": (0.18, 0.92),
            "F7":  (-0.71, 0.55), "F3":  (-0.40, 0.58), "Fz": (0.00, 0.60),
            "F4":  (0.40, 0.58),  "F8":  (0.71, 0.55),
            "T3":  (-0.87, 0.00), "C3":  (-0.50, 0.00), "Cz": (0.00, 0.00),
            "C4":  (0.50, 0.00),  "T4":  (0.87, 0.00),
            "T5":  (-0.71, -0.55), "P3": (-0.40, -0.58), "Pz": (0.00, -0.60),
            "P4":  (0.40, -0.58),  "T6": (0.71, -0.55),
            "O1":  (-0.18, -0.92), "Oz": (0.00, -0.95), "O2": (0.18, -0.92)
        }
        self.graph = nx.Graph()
        self.fig = mpl.figure()
    
    def update(self, snapshot):
        for i in snapshot:
            weights = snapshot.get(i)
            self.graph.add_edge(i[0],i[1],weight = weights[0])
            
    def animate(self, frame):
        self.fig.clear()
        nodes = {electrode: self.positions[electrode] for electrode in self.graph.nodes() if electrode in self.positions}
        weights = self.graph.edges.data("weight",default = 0)
        shownEdges = [edge for edge in weights if edge[2] > 0.1]
        edgeWidths = [edge[2] * 10 + 1 for edge in shownEdges]
        nx.draw(self.graph, pos = nodes, edgelist = shownEdges, width = edgeWidths, with_labels = True)
    
    def show(self):
        self.ani = ani.FuncAnimation(self.fig,self.animate,interval = 100,cache_frame_data = False)
        mpl.show()
        

