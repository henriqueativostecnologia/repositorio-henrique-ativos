import json,glob,os
from collections import Counter,defaultdict
F34="position, title, place_id, data_id, data_cid, reviews_link, photos_link, gps_coordinates, place_id_search, provider_id, rating, reviews, price, extracted_price, type, types, type_id, type_ids, address, country, open_state, hours, operating_hours, phone, website, amenities, description, service_options, order_online, thumbnail, serpapi_thumbnail, extensions, unsupported_extensions, user_review".split(', ')
assert len(F34)==34 and len(set(F34))==34
def cheio(v): return not (v is None or v=='' or v==[] or v=={})
lojas=[]; extra=Counter(); extra_ex={}; porbusca=defaultdict(list); info={}; err=[]
for f in sorted(glob.glob('raw/*.json')):
  d=json.load(open(f)); m=d.get('search_metadata',{})
  if not m.get('created_at','').startswith('2026-10-15'): continue
  if 'error' in d: err.append((os.path.basename(f),d.get('error'),d.get('search_parameters',{}).get('q')))
  p=d.get('search_parameters',{}); info[f]=p
  for bloco in ('local_results','ads'):
    for it in d.get(bloco,[]) or []:
      pres=[k for k in F34 if cheio(it.get(k))]
      for k in it:
        if k not in F34: extra[k]+=1; extra_ex.setdefault(k,(it[k] if not isinstance(it[k],(dict,list)) else json.dumps(it[k],ensure_ascii=False)[:120]))
      pct=len(pres)/34*100
      x=dict(f=f,bloco=bloco,title=it.get('title'),q=p.get('q'),ll=p.get('ll'),start=p.get('start'),n=len(pres),pct=pct,falta=[k for k in F34 if k not in pres],place_id=it.get('place_id'),item=it)
      lojas.append(x); porbusca[f].append(pct)
print('arquivos de 15/10:',len(info),'| com local_results:',sum(1 for f in info if porbusca[f]),'| itens (lojas):',len(lojas),'| ads:',sum(1 for x in lojas if x['bloco']=='ads'))
print('erros:',err)
top=sorted(lojas,key=lambda x:(-x['pct'],x['title']))
print('maior n de campos:',top[0]['n'],'| quantas empatam:',sum(1 for x in lojas if x['n']==top[0]['n']))
for x in top[:8]: print(x['n'],round(x['pct'],4),x['title'],'|',x['q'],x['ll'],x['start'],'| faltam:',x['falta'])
med={f:sum(v)/len(v) for f,v in porbusca.items() if v}
rk=sorted(med.items(),key=lambda kv:-kv[1])
print('buscas com média:',len(med))
for f,v in rk[:8]: print(round(v,4),info[f].get('q'),info[f].get('ll'),info[f].get('start'),len(porbusca[f]),os.path.basename(f))
print('...menor:',[(round(v,4),info[f].get('q'),info[f].get('ll')) for f,v in rk[-3:]])
print('campos fora dos 34:',dict(extra)); print({k:extra_ex[k] for k in extra})
json.dump(dict(top=[{k:v for k,v in x.items() if k!='item'} for x in top[:5]],rk=[(os.path.basename(f),v,info[f]) for f,v in rk],best_item_file=top[0]['f'],best_item_pid=top[0]['place_id']),open('fill_res.json','w'),ensure_ascii=False)
