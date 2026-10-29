import sys,json,math;sys.path.insert(0,'.')
from bh import load,bairro,regional
R=load(lambda p: str(p.get('ll','')).endswith('15z') and p.get('q') in ('cafeteria','padaria','armazém empório'))
SEG={'Padaria':'Padaria','Cafeteria':'Cafeteria','Café':'Cafeteria','Confeitaria':'Cafeteria','Loja de café':'Cafeteria','Espresso bar':'Cafeteria','Restaurante de brunch':'Cafeteria',
     'Armazém':'Armazém','Empório gourmet':'Armazém','Mercearia':'Armazém','Loja de produtos naturais':'Armazém','Loja de alimentos orgânicos':'Armazém'}
FRACO=('instagram.com','linktr.ee','facebook.com','fb.com','wa.me','whatsapp','ifood.com','ola.click','beacons.ai','g.co/','g.page','lojalocal.com','agendaservico','anota.ai','goomer','aiqfome','cardapio')
ENCURT=('bit.ly','abrir.link')
SIMPLES=('site123.me','sites.google.com','wixsite.com')
REDE=('redeexemploa','redeexemplob')  # exemplos: trocar por pedaços do site de redes/franquias da região
HOME=(-19.8631,-43.9535)
def km(a,b):
  dx=(a[1]-b[1])*111.320*math.cos(math.radians(-19.86)); dy=(a[0]-b[0])*110.574; return math.hypot(dx,dy)
L=[]
for r in R.values():
  a=r.get('address') or ''
  if 'Belo Horizonte' not in a or r.get('type') not in SEG or 'Marketplace Exemplo' in r['title']: continue
  w=(r.get('website') or '').lower(); rt=r.get('rating'); rv=r.get('reviews')
  obs=[]
  if not w: grupo='Sem site / só rede social'; tipo_site='sem site'
  elif any(k in w for k in FRACO): grupo='Sem site / só rede social'; tipo_site='só rede social / delivery / ficha'
  elif any(k in w for k in ENCURT): grupo='Sem site / só rede social'; tipo_site='link encurtado'; obs.append('site é um link encurtado: conferir para onde leva')
  else:
    grupo='Com site (modernizar)'; tipo_site='site próprio'
    if any(k in w for k in SIMPLES): obs.append('site em construtor gratuito (subdomínio): simples')
  if any(k in w for k in REDE): obs.append('rede/franquia: decisão pode não ser local')
  melhor=int(grupo.startswith('Sem') and rt is not None and rt>=4.5)
  ativo=int(rv is not None and rv>=10)
  if rt is not None and rt<4.0: obs.append(f'cuidado: nota {rt} abaixo de 4,0')
  b=bairro(a); b=b.split(',')[-1].strip() if b and ',' in b else b; g=r['gps_coordinates']
  if 'Padaria Exemplo' in r['title']: obs.append('rede local (Padaria Exemplo tem mais de uma unidade)')
  L.append(dict(grupo=grupo,seg=SEG[r['type']],nome=r['title'],bairro=b,reg=regional(b),end=a,tel=r.get('phone'),site=r.get('website'),nota=rt,aval=rv,
    km=km(HOME,(g['latitude'],g['longitude'])),melhor=melhor,ativo=ativo,tipo_site=tipo_site,obs='; '.join(obs),link=f"https://www.google.com/maps/place/?q=place_id:{r['place_id']}"))
key=lambda x:(-(x['melhor'] and x['ativo']),x['km'])
L.sort(key=key)
json.dump(L,open('alim.json','w'),ensure_ascii=False)
from collections import Counter
print(len(L),Counter(x['grupo'] for x in L),Counter((x['grupo'],x['melhor'] and x['ativo']) for x in L))
print(Counter(x['seg'] for x in L), Counter(x['reg'] for x in L))
for x in L:
  if x['grupo'].startswith('Com'): print(round(x['km'],2),x['seg'],'|',x['nome'][:40],'|',x['bairro'],'|',x['nota'],x['aval'],'|',x['site'][:50],'|',x['obs'])
