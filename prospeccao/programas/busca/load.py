import json,glob,math,re
def allres():
  out={}
  for f in glob.glob('raw/*.json'):
    d=json.load(open(f)); q=d.get('search_parameters',{}).get('q','')
    if d.get('search_parameters',{}).get('engine')!='google_maps': continue
    for r in d.get('local_results',[]) or []:
      pid=r.get('place_id'); 
      if pid not in out: out[pid]=dict(r,_q=[q])
      else: out[pid]['_q'].append(q)
  return out
