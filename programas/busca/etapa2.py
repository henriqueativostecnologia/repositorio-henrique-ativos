import sys,json,glob;sys.path.insert(0,'.')
from serp import search
from bh import *
from collections import Counter
isE1=lambda p: p.get('q') in ('estética automotiva','lava jato') and str(p.get('ll','')).endswith('14z') and not p.get('start')
by={}
for f in glob.glob('raw/*.json'):
  d=json.load(open(f)); p=d.get('search_parameters',{})
  if isE1(p): by.setdefault(p['ll'],[]).extend(r for r in d.get('local_results',[]) if 'Belo Horizonte' in (r.get('address') or ''))
PTS=[ll for ll,rs in by.items() if rs and Counter(regional(bairro(r['address'])) for r in rs).most_common(1)[0][0] in ('Pampulha','Venda Nova')]
print('pontos',len(PTS),PTS)
json.dump(PTS,open('pts_etapa2.json','w'))
base=lambda q,ll,**k: dict(engine='google_maps',type='search',q=q,ll=ll,hl='pt-br',gl='br',**k)
n=0
for ll in PTS:
  for q in ['detailing polimento vitrificação','insulfilm envelopamento','martelinho de ouro','revenda de seminovos']:
    d=search(base(q,ll)); n+=1
  for q in ['estética automotiva','lava jato']:
    full=len(search(base(q,ll)).get('local_results',[]))>=20
    for st in (20,40):
      if not full: break
      d=search(base(q,ll,start=st)); n+=1; full=len(d.get('local_results',[]) or [])>=20
print('buscas novas',n)
