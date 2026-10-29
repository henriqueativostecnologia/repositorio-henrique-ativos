import json,sys
sys.path.insert(0,'.')
from serp import search
cats=["restaurante","cafeteria","padaria","bar","armazém empório mercearia","estética automotiva lava jato","compra e venda de veículos"]
pts={"sul":"@-19.9815,-43.9440,17z","norte":"@-19.9762,-43.9395,17z"}
for c in cats:
  for n,ll in pts.items():
    d=search({"engine":"google_maps","type":"search","q":c,"ll":ll,"hl":"pt-br","gl":"br"})
    lr=d.get("local_results",[])
    print(c,n,len(lr),"next" if d.get("serpapi_pagination",{}).get("next") else "", d.get("error",""))
