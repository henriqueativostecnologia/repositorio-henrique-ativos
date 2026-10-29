import sys,json,math;sys.path.insert(0,'.')
exec(open('build2.py').read().split('key=lambda')[0])  # reaproveita a montagem de L da etapa 2 (mesmos dados, sem buscas)
F=[x for x in L if not x['f']['fraca']]
HOME=(-19.8600,-43.9550)
def km(a,b):
  dx=(a[1]-b[1])*111.320*math.cos(math.radians(-19.85)); dy=(a[0]-b[0])*110.574; return math.hypot(dx,dy)
for x in F: x['km']=km(HOME,(x['r']['gps_coordinates']['latitude'],x['r']['gps_coordinates']['longitude']))
for x in sorted(F,key=lambda x:(x['g']!='Pampulha',x['km'])):
  r=x['r']; print(round(x['km'],2),'|',x['g'],'|',x['seg'],'|',r['title'][:40],'|',r.get('rating'),r.get('reviews'),'|',r.get('website'))
json.dump([dict(nome=x['r']['title'],seg=x['seg'],b=x['b'],g=x['g'],km=x['km'],r={k:x['r'].get(k) for k in ('address','phone','website','rating','reviews','place_id')}) for x in F],open('fortes.json','w'),ensure_ascii=False)
