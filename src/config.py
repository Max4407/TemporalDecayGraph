from enum import Enum
class bands(Enum):    #different frequency bands for switching visualizer
    Delta = 0
    Theta = 1
    Alpha = 2
    Beta = 3
    Gamma = 4
    
BAND_DISPLAYED = bands.Beta   #change to view a different band in visualizer
DECAY_RATE = 0.7 #value between 0 and 1, closer to zero will decay faster
PRUNING_CUTOFF = 0.85 #value to prune values that are getting low, which reduces noise and makes the visualizer easier to read
DATA_HZ = 6 #how many windows per second in the .csv data file
