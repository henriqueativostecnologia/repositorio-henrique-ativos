import math
# contorno aproximado do município de BH (lat, lon), só para escolher os pontos da grade
POLY=[(-19.776,-43.95),(-19.79,-43.91),(-19.83,-43.88),(-19.87,-43.86),(-19.92,-43.857),(-19.95,-43.88),(-19.975,-43.92),(-19.98,-43.95),(-19.99,-43.98),(-20.03,-44.01),(-20.059,-44.03),(-20.04,-44.063),(-19.99,-44.06),(-19.96,-44.03),(-19.93,-44.02),(-19.88,-44.03),(-19.84,-44.02),(-19.80,-44.00),(-19.78,-43.98)]
def inside(lat,lon):
  c=False;n=len(POLY)
  for i in range(n):
    (y1,x1),(y2,x2)=POLY[i],POLY[(i+1)%n]
    if (y1>lat)!=(y2>lat) and lon < (x2-x1)*(lat-y1)/(y2-y1)+x1: c=not c
  return c
def grid(step_km):
  dlat=step_km/110.574; dlon=step_km/(111.320*math.cos(math.radians(-19.92)))
  pts=[];lat=-20.059+dlat/2
  while lat<-19.776:
    lon=-44.063+dlon/2
    while lon<-43.857:
      if inside(lat,lon): pts.append((round(lat,4),round(lon,4)))
      lon+=dlon
    lat+=dlat
  return pts
if __name__=='__main__':
  for s in (3,6): print(s,len(grid(s)))
