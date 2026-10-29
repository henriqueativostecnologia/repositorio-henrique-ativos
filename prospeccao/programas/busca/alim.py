import sys;sys.path.insert(0,'.')
from serp import search
PTS={'a':'@-19.8631,-43.9535,15z','b':'@-19.8657,-43.9741,15z','c':'@-19.8385,-43.9702,15z'}
n=0
for k,ll in PTS.items():
  for q in ['cafeteria','padaria','armazém empório']:
    d=search(dict(engine='google_maps',type='search',q=q,ll=ll,hl='pt-br',gl='br')); n+=1
    c=len(d.get('local_results',[]) or []); p2=''
    if c>=20:
      d2=search(dict(engine='google_maps',type='search',q=q,ll=ll,hl='pt-br',gl='br',start=20)); n+=1; p2=len(d2.get('local_results',[]) or [])
    print(k,q,c,p2)
print('buscas',n)
