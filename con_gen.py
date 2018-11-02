import json
import numpy as np
from itertools import product
neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1]]
windowsize0 = [[0,0]]
windowsize1 = [[0,0],[1,0],[1,-1],[0,-1],[-1,0],[-1,1],[0,1]]
windowsize2 = [[0,0],[1,0],[1,-1],[0,-1],[-1,0],[-1,1],[0,1],[1,1],[2,0],[2,-1],[2,-2],[1,-2],[0,-2],[-1,-1],[-2,0],[-2,1],[-2,2],[-1,2],[0,2]]
windows["0"] = windowsize0
windows["1"] = windowsize1
windows["2"] = windowsize2

#layer_name = ["R1-6","L1","L3","L5","Mi1","Tm3","Mi4","Mi9","TmY15","CT1","C1"]
#dynamics = ["R","L","L","L","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1"]
# layer size
w = 1
h = 1
cells = []
with open("./connection_window.json","r") as f:
    connection = json.load(f)

net = []
for con in connection:
    target = con["target"]
    for src in con["sources"]:
        print(src)
        for x,y in product(range(w),range(h)):
            n = {}
            n["target_synapse"] = con["synapse"]
            n["synapse_opt"] = con["synapse_opt"]
            for coord in windows[str(src["windowsize"])]:
                if x + coord[0]< 0 or x + coord[0]>= w:
                    continue
                if y + coord[1]< 0 or y + coord[1]>= h:
                    continue
                n["target_cellname"] = con["target"] + "," + str(x) + "," + str(y)
                n["source_cellname"] = src["source"] + "," + str(x+coord[0]) + "," + str(y+coord[1])
                n["source_section"] = src["section"]
                synlist = src["num_synapse"]
                n["synapse_opt"]["numsyn"] = synlist[0]
                if "source_opt" in src:
                    n["source_opt"] = src["source_opt"]
                else:
                    n["source_opt"] = {}
            net.append(n)

print(net)
with open("./nwk.json","w") as f:
    json.dump(net,f, indent=4, sort_keys=True, separators=(',', ': '))
