import sys,json;sys.path.insert(0,'.')
from serp import search; from grid import grid
err=0
for lat,lon in grid(3):
  for q in ['estética automotiva','lava jato']:
    try:
      d=search({'engine':'google_maps','type':'search','q':q,'ll':f'@{lat},{lon},14z','hl':'pt-br','gl':'br'})
      if 'local_results' not in d: err+=1; print('sem resultado',lat,lon,q,str(d)[:200])
    except Exception as e: err+=1; print('ERRO',lat,lon,q,e)
print('erros',err)
