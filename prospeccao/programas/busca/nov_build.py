import sys,json,glob,math,re;sys.path.insert(0,'.')
from bh import load,bairro,regional,norm
from collections import Counter
HOME=(-19.8631,-43.9535)
def km(g): 
  return math.hypot((g['longitude']-HOME[1])*111.320*math.cos(math.radians(-19.86)),(g['latitude']-HOME[0])*110.574)
REDE_SOC=('instagram.com','linktr.ee','facebook.com','fb.com','ifood.com')
OUTRO_FRACO={'wa.me':'link de WhatsApp','whatsapp':'link de WhatsApp','beacons.ai':'página de links (Beacons)','ola.click':'cardápio online','g.page':'link da ficha do Google','g.co/':'link da ficha do Google','agendaservico':'página de agendamento','bit.ly':'link encurtado','abrir.link':'link encurtado','linkbio':'página de links','bio.site':'página de links'}
SIMPLES=('sites.google.com','site123.me','wixsite.com','webnode','negocio.site','business.site')
REDES=['rede exemplo a','rede exemplo b','franquia exemplo']  # exemplos: trocar pelos nomes (em minúsculas) das redes/franquias
def site_info(w):
  wl=(w or '').lower()
  if not wl: return 'Não','sem site',True
  if any(k in wl for k in REDE_SOC): 
    k=next(k for k in REDE_SOC if k in wl); return 'Não',{'instagram.com':'"site" é só Instagram','linktr.ee':'"site" é só Linktree','facebook.com':'"site" é só Facebook','fb.com':'"site" é só Facebook','ifood.com':'"site" é só iFood'}[k],True
  for k,v in OUTRO_FRACO.items():
    if k in wl: return 'Não',f'"site" é só {v}',False   # fraco, mas fora da regra de melhor alvo do Henrique
  if any(k in wl for k in SIMPLES): return 'Sim','site em construtor gratuito (simples)',None
  return 'Sim','',None
QSEG={'revenda de carros seminovos':('Automotivo','Revenda de seminovos'),'imobiliária':('Imobiliário','Imobiliária'),'construtora':('Imobiliário','Construtora'),
      'advogado trabalhista':('Advocacia','Advogado trabalhista'),'advogado previdenciário':('Advocacia','Advogado previdenciário'),'doceria':('Alimentação','Doceria'),'restaurante':('Alimentação','Restaurante')}
INCL_NE={'PALMARES','SANTA CRUZ'}
HOJE=[json.loads(l) for l in open('calls.log').read().splitlines()[-35:]]
HOJE_K={(h['q'],h['ll']) for h in HOJE}
assert len(HOJE_K)==35
R={}
for f in glob.glob('raw/*.json'):
  d=json.load(open(f)); p=d.get('search_parameters',{})
  if (p.get('q'),p.get('ll')) not in HOJE_K: continue
  for r in d.get('local_results',[]) or []:
    x=R.setdefault(r['place_id'],dict(r,_q=set())); x['_q'].add(p['q'])
rows=[]; drop=Counter()
def area(b,g):
  if g in ('Pampulha','Venda Nova'): return True
  return norm(b or '') in INCL_NE
for r in R.values():
  a=r.get('address') or ''
  if 'Belo Horizonte' not in a: drop['fora de BH']+=1; continue
  b=(bairro(a) or '').split(',')[-1].strip(); g=regional(b)
  if not area(b,g):
    drop['fora da área' if g!='A conferir' else 'regional a conferir (fora)']+=1; continue
  qs=r['_q']
  if {'advogado trabalhista','advogado previdenciário'}<=qs: setor,seg='Advocacia','Advogado trabalhista e previdenciário'
  else:
    order=list(QSEG); q=sorted(qs,key=order.index)[0]; setor,seg=QSEG[q]
  rows.append(dict(r=r,setor=setor,seg=seg,b=b,g=g))
# estéticas COM site de 15/10 (sem gastar busca)
_NOVO=R
exec(open('build2.py').read().split('key=lambda')[0])
R=_NOVO
ext=0
for x in L:
  if x['seg']=='Revenda de seminovos': continue
  tem,_,_=site_info(x['r'].get('website'))
  if tem=='Sim' and x['r']['place_id'] not in R:
    rows.append(dict(r=x['r'],setor='Automotivo',seg=x['seg']+' (dados de 15/10)',b=x['b'],g=x['g'])); ext+=1
# redes: nome conhecido ou mesma marca em mais de uma unidade
GEN={'RESTAURANTE','LAVA','JATO','IMOBILIARIA','CONFEITARIA','DOCERIA','DOCES','ADVOCACIA','ADVOGADOS','ADVOGADO','CONSTRUTORA','BAR','E','DE','DO','DA','O','A','PIZZARIA','CHURRASCARIA','ESTETICA','AUTOMOTIVA','MARTELINHO','OURO','SEMINOVOS','VEICULOS'}
def marca(t): return ' '.join([w for w in norm(re.split(r'[-|–(]',t)[0]).split() if w not in GEN][:2])
cnt=Counter(marca(x['r']['title']) for x in rows)
out=[]
for x in rows:
  r=x['r']; tem,motivo,regra=site_info(r.get('website')); rt=r.get('rating'); rv=r.get('reviews')
  obs=[]
  if motivo: obs.append(motivo)
  tl=r['title'].lower()
  if any(k in tl or k in (r.get('website') or '').lower() for k in REDES): obs.append('franquia/rede grande')
  melhor= 'SIM' if (tem=='Não' and regra is True and rt is not None and rt>=4.5) else ''
  if tem=='Não' and regra is False and rt is not None and rt>=4.5: obs.append('nota alta, mas o link não está na regra de melhor alvo (conferir)')
  ativo='SIM' if (rv is not None and rv>=10) else ''
  if x['setor']=='Advocacia' or x['seg']=='Construtora':
    if not ativo: obs.append('poucas avaliações (menos de 10): comum no setor')
  if 'advogado criminal' in (r.get('type') or '').lower() or 'imobiliário' in (r.get('type') or '').lower() and x['setor']=='Advocacia': obs.append(f"no Google: {r.get('type')}")
  if rt is not None and rt<4.0: obs.append(f'cuidado: nota {rt} abaixo de 4,0')
  if x['g']=='A conferir': obs.append('regional a conferir')
  out.append(dict(setor=x['setor'],seg=x['seg'],tem=tem,nome=r['title'],reg=x['g'],b=x['b'] or '(sem bairro no endereço)',end=r.get('address'),tel=r.get('phone'),site=r.get('website'),nota=rt,aval=rv,km=km(r['gps_coordinates']),melhor=melhor,ativo=ativo,obs='; '.join(obs),link=f"https://www.google.com/maps/place/?q=place_id:{r['place_id']}"))
# fichas duplicadas no Google (mesmo nome e mesmo telefone ou mesmo endereço até o número)
grp={}
for x in out:
  k=(norm(x['nome']), x['tel'] or norm((x['end'] or '').split(' - ')[0]))
  grp.setdefault(k,[]).append(x)
dup=0; out2=[]
for k,v in grp.items():
  x=v[0]
  if len(v)>1:
    dup+=len(v)-1; x['obs']=(x['obs']+'; ' if x['obs'] else '')+f'{len(v)} fichas no Google para a mesma loja (duplicadas)'
  out2.append(x)
out=out2
if 'Instituição Exemplo' in ' '.join(x['nome'] for x in out):
  for x in out:
    if 'Restaurante Exemplo da Instituição' in x['nome']: x['obs']=(x['obs']+'; ' if x['obs'] else '')+'restaurante público: provavelmente não é alvo'
out.sort(key=lambda x:(norm(x['b']),x['seg'],x['nome']))
json.dump(dict(out=out,drop=drop,ext=ext,uniq=len(R),dup=dup),open('nov.json','w'),ensure_ascii=False,default=str)
print('únicas nas buscas',len(R),'| fora',dict(drop),'| estéticas c/ site 15/10',ext,'| linhas',len(out))
S=Counter(); 
for x in out:
  k=x['seg'].replace(' (dados de 15/10)',''); S[(k,'tot')]+=1; S[(k,'sem')]+= x['tem']=='Não'; S[(k,'mel')]+= bool(x['melhor'] and x['ativo'])
for k in sorted({k for k,_ in S}): print(k,S[(k,'tot')],S[(k,'sem')],S[(k,'mel')])
print(Counter(x['b'] for x in out).most_common(40))
