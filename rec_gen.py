import json
import numpy as np
from itertools import product
neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1]]

layer_name = ["R1-6","L1","L3","L5","Mi1","Tm3","Mi4","Mi9","TmY15","CT1","C2","C3","T4a","T4b","T4c","T4d"]
dynamics = ["R","L","L","L","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1"]
# layer size
w = 35
h = 40

with open("./record_position.json","r") as f:
    recs = json.load(f)

cells = []
for rec in recs:
    for x,y in product(range(w),range(h)):
        conf = {}
        conf["target_cellname"] = rec["target"] + "," + str(x) + "," + str(y)
        conf["section"] = rec["section"]
        cells.append(conf)

with open("./rec.json","w") as f:
    json.dump(cells,f, indent=4, sort_keys=True, separators=(',', ': '))
