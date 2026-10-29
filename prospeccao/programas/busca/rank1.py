import sys,json,glob;sys.path.insert(0,'.')
from bh import *
from collections import Counter,defaultdict
isE1=lambda p: p.get('q') in ('estética automotiva','lava jato') and str(p.get('ll','')).endswith('14z')
R=load(isE1)
L=[]
for r in R.values():
  a=r.get('address') or ''
  if 'Belo Horizonte' not in a or r.get('type') in EXCL: continue
  b=bairro(a); g=regional(b); f=flags(r)
  L.append(dict(r=r,b=b,g=g,f=f))
# pontos da grade por regional: regional mais comum entre os resultados em BH de cada ponto
pts=defaultdict(Counter)
for fp in glob.glob('raw/*.json'):
  d=json.load(open(fp)); p=d.get('search_parameters',{})
  if not isE1(p): continue
  for r in d.get('local_results',[]) or []:
    if 'Belo Horizonte' in (r.get('address') or ''): pts[p['ll']][regional(bairro(r['address']))]+=1
P=Counter(c.most_common(1)[0][0] for c in pts.values() if c)
T=defaultdict(lambda: Counter())
for x in L:
  t=T[x['g']]; t['total']+=1
  for k in ('sem_site','social','poucas','fraca','melhor','cuidado'): t[k]+=x['f'][k]
rows=[]
for g in REGIONAIS+['A conferir']:
  t=T[g]; pct=t['fraca']/t['total'] if t['total'] else None
  rows.append(dict(g=g,pts=P.get(g,0),**t,pct=pct))
json.dump(dict(rows=rows,L=[dict(nome=x['r']['title'],g=x['g'],b=x['b'],f=x['f'],r={k:x['r'].get(k) for k in ('address','phone','website','rating','reviews','type','place_id','gps_coordinates')}) for x in L]),open('etapa1.json','w'),ensure_ascii=False)
for r in sorted(rows,key=lambda r:-r['fraca']): print(r['g'],'| pontos',r['pts'],'| total',r['total'],'| sem site',r['sem_site'],'| social',r['social'],'| <30',r['poucas'],'| fraca',r['fraca'],'| %', None if r['pct'] is None else round(100*r['pct'],2),'| melhor',r['melhor'])
print('total',len(L), 'pontos sem resultado em BH', 43-sum(P.values()))
