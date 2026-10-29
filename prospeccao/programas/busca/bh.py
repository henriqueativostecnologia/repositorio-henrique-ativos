import json,glob,re,unicodedata
def norm(s): return re.sub(r'\s+',' ',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().upper().replace('-',' ')).strip()
REG={}
for l in open('bairros_pbh.txt',encoding='utf-8'):
  b,r=l.strip().split('|'); REG[norm(b)]=r.title().replace('Centro-Sul','Centro-Sul')
ALIAS={'NOVA SUICA':'NOVA SUISSA','SAO LUIZ':'SAO LUIZ','SAO LUIS':'SAO LUIZ','CAICARA':'CAICARAS','CAICARA ADELAIDE':'CAICARA ADELAIDE','PADRE EUSTAQUIO':'PADRE EUSTAQUIO','SANTA MONICA':'SANTA MONICA','CIDADE NOVA':'CIDADE NOVA','BAIRRO DAS INDUSTRIAS':'BAIRRO DAS INDUSTRIAS I','ALIPIO DE MELLO':'ALIPIO DE MELO','PALMARES':'PALMARES','SANTA EFIGENIA':'SANTA EFIGENIA','JARDIM DOS COMERCIARIOS':'JARDIM DOS COMERCIARIOS','LOURDES':'LOURDES','SANTO ANTONIO':'SANTO ANTONIO','FLORESTA':'FLORESTA','HELIOPOLIS':'HELIOPOLIS','TUPI':'TUPI A','BARAO HOMEM DE MELO':'BARAO HOMEM DE MELO I','SAO JORGE':'SAO JORGE I','MARIETA':'MARIETA I','CAMPONESA':'CAMPONES A I','JARDIM MONTANHES':'JARDIM MONTANHES','DOM BOSCO':'DOM BOSCO','GOIANIA':'GOIANIA'}
def bairro(addr):
  if not addr or 'Belo Horizonte' not in addr: return None
  pre=addr.split(', Belo Horizonte')[0]
  b=pre.split(' - ')[-1].strip() if ' - ' in pre else ''
  return b
def regional(b):
  if not b: return 'A conferir'
  n=norm(b); n=ALIAS.get(n,n)
  if n in REG: return REG[n]
  n2=re.sub(r'^(BAIRRO|VILA|CONJUNTO) ','',n)
  if n2 in REG: return REG[n2]
  n3=re.sub(r' (I|II|III|IV|V|\d+[A-Z]? SECAO)$','',n)
  if n3 in REG: return REG[n3]
  for k in (n+' I',):
    if k in REG: return REG[k]
  return 'A conferir'
SOCIAL=('instagram.com','linktr.ee','facebook.com','fb.com','wa.me','web.app','linkbio','bio.site','beacons.ai')
def flags(r):
  w=(r.get('website') or '').lower(); rv=r.get('reviews'); rt=r.get('rating')
  f={'sem_site':int(not w),'social':int(bool(w) and any(s in w for s in SOCIAL)),'poucas':int(rv is None or rv<30)}
  f['fraca']=int(any(f.values())); f['cuidado']=int(rt is not None and rt<4.0)
  f['melhor']=int(rt is not None and rt>=4.5 and bool(f['fraca']))
  return f
def load(filter_fn):
  out={}
  for fpath in glob.glob('raw/*.json'):
    d=json.load(open(fpath)); p=d.get('search_parameters',{})
    if not filter_fn(p): continue
    for r in d.get('local_results',[]) or []:
      pid=r['place_id']
      if pid in out: out[pid]['_q'].add(p.get('q'))
      else: out[pid]=dict(r,_q={p.get('q')})
  return out
REGIONAIS=['Barreiro','Centro-Sul','Leste','Nordeste','Noroeste','Norte','Oeste','Pampulha','Venda Nova']
_reg_old=regional
def regional(b):
  if not b: return 'A conferir'
  m=re.match(r'^(.*?)\s*\((.*)\)\s*$',b)
  if m:
    base,par=m.group(1),m.group(2)
    r=_reg_old(base)
    if r=='A conferir': r=_reg_old(base.split()[0]) if base.split() else r
    if norm(par) in [norm(x) for x in REGIONAIS] and r!='A conferir' and norm(r)!=norm(par): return 'A conferir'
    return r
  return _reg_old(b)
EXCL={'Estacionamento','Departamento de veículos automotores','Depósito','Padaria atacadista','Estúdio de pintura','Mecânica para carros','Oficina mecânica'}
