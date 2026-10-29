import math
# polilinha da Alameda Oscar Niemeyer, tirada das coordenadas dos próprios comércios com endereço nela (sul -> norte)
P=[(-19.98379,-43.94616),(-19.98332,-43.94558),(-19.98170,-43.94416),(-19.98053,-43.94344),(-19.97810,-43.94223),(-19.97705,-43.94077),(-19.97579,-43.93956),(-19.97524,-43.93770)]
def xy(p): return (p[1]*111320*math.cos(math.radians(-19.98)), p[0]*110574)
def dist_av(lat,lon):
  px,py=xy((lat,lon)); best=(1e9,0); acc=0
  for i in range(len(P)-1):
    (ax,ay),(bx,by)=xy(P[i]),xy(P[i+1]); dx,dy=bx-ax,by-ay; L=math.hypot(dx,dy)
    t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/(L*L))); d=math.hypot(px-(ax+t*dx),py-(ay+t*dy))
    if d<best[0]: best=(d,acc+t*L)
    acc+=L
  return best  # (distância em m, posição ao longo da avenida em m a partir do sul)
