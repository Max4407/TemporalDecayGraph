import matplotlib.pyplot as mpl
import matplotlib.animation as ani
import networkx as nx 

from config import PRUNING_CUTOFF, BAND_DISPLAYED

class EEGVisualizer: 
    def __init__(self):
        self.positions = {
            "Fp1":  (-0.20, 0.87), "Fpz":  (0.00, 0.90), "Fp2":  (0.20, 0.87),
            "F7":   (-0.72, 0.52), "F3":   (-0.42, 0.52), "Fz":   (0.00, 0.54),
            "F4":   (0.42, 0.52),  "F8":   (0.72, 0.52),
            "T3":   (-0.90, 0.00), "C3":   (-0.46, 0.00), "Cz":   (0.00, 0.00),
            "C4":   (0.46, 0.00),  "T4":   (0.90, 0.00),
            "T5":   (-0.72, -0.52), "P3":  (-0.42, -0.52), "Pz":  (0.00, -0.54),
            "P4":   (0.42, -0.52),  "T6":  (0.72, -0.52),
            "O1":   (-0.20, -0.87), "Oz":  (0.00, -0.90), "O2":  (0.20, -0.87),
            "A2-A1": (1.15, 0.00),
        }
        self.graph = nx.Graph()
        self.fig, self.axes = mpl.subplots()
        self.title = "baseline"
    
    def update(self, snapshot,title):
        for i in snapshot:
            weights = snapshot.get(i)
            self.graph.add_edge(i[0],i[1],weight = weights[BAND_DISPLAYED.value])
        self.title = title
            
    def animate(self, frame):
        self.axes.clear()
        self.axes.annotate(self.title,(1,1))
        nodes = {electrode: self.positions[electrode] for electrode in self.graph.nodes() if electrode in self.positions}
        weights = self.graph.edges.data("weight",default = 0)
        shownEdges = [edge for edge in weights if edge[2] > PRUNING_CUTOFF]
        edgeWidths = [(edge[2] - PRUNING_CUTOFF) * 25 for edge in shownEdges]
        nx.draw(self.graph, pos = nodes, edgelist = shownEdges, width = edgeWidths, with_labels = True)
        self.axes.set_xlim(-1, 1.3)
        self.axes.set_ylim(-1, 1)
        self.axes.set_aspect("equal")
    
    def show(self):
        self.ani = ani.FuncAnimation(self.fig,self.animate,interval = 5,cache_frame_data = False)
        mpl.show()
    
    def close(self):
        mpl.close('all')
        

