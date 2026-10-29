import sys,json;sys.path.insert(0,'.')
from serp import search
ll='@-19.9230,-43.9600,15z'
Q=['estética automotiva lava jato','estética automotiva','detailing polimento vitrificação','lava jato','insulfilm envelopamento','martelinho de ouro']
S={}
for q in Q:
  d=search({'engine':'google_maps','type':'search','q':q,'ll':ll,'hl':'pt-br','gl':'br'})
  S[q]={r['place_id']:(r['title'],r.get('type')) for r in d.get('local_results',[])}
  print(q,len(S[q]))
comb=set(S[Q[0]]); 
for q in Q[1:]:
  s=set(S[q]); print(f'{q}: {len(s)} | também na juntada: {len(s&comb)} | só na separada: {len(s-comb)}')
sep3=set().union(*[set(S[q]) for q in Q[1:4]])
print('união estética+detailing+lava jato:',len(sep3),'achadas pela juntada:',len(sep3&comb))
print('tipos na juntada:',sorted(set(t for _,t in S[Q[0]].values())))
for q in Q[4:]: print(q,'tipos:',sorted(set(str(t) for _,t in S[q].values())))
