import json
import numpy as np
from itertools import product
neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1]]

layer_name = ["R1-6","L1","L2","L3","L4","L5","Mi1","Tm3","Mi4","Mi9","TmY15","CT1","C2","C3","T4a","T4b","T4c","T4d"]
dynamics = ["R","L","L","L","L","L","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1"]
# layer size
w = 10
h = 10
stims = []
stim_timing = [[300,1100,1]]
for st in stim_timing:
    for x,y in product(range(w),range(h)):
        stim = {}
        stim["stimulator"] = "BellCurrent"
        stim["target_cellname"] = "R1-6" + "," + str(x) + "," + str(y)
        stim["section"] = {"name":"axon","point":0.5}
        stim["opt"] = {}
        stim["opt"]["st"] = st[0]
        stim["opt"]["en"] = st[1]
        stim["opt"]["amp"] = st[2]
        stim["opt"]["slope"] = 0.03
        stims.append(stim)

with open("./wholestm.json","w") as f:
    json.dump(stims,f)
