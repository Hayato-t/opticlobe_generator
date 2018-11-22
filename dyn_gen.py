import json
import numpy as np
from itertools import product
neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1]]

layer_name = ["R1-6","L1","L2","L3","L4","L5","Mi1","Tm3","Mi4","Mi9","TmY15","CT1","C2","C3","T4a","T4b","T4c","T4d"]
dynamics = ["R","L","L","L","L","L","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1"]
# layer size
w = 10
h = 10
cells = []
for i,name in enumerate(layer_name):
    for x,y in product(range(w),range(h)):
        cell = {}
        cell["cellname"] = name + "," + str(x) + "," + str(y)
        cell["celltype"] = dynamics[i]
        cell["params"] = {}
        cells.append(cell)

with open("./dyn.json","w") as f:
    json.dump(cells,f)
