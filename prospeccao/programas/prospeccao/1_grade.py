# Passo 1: escolhe os pontos de busca dentro da área (ou até "borda_km" da borda).
# Uso: python3 1_grade.py dados/config.json dados/bairros.geojson dados/pontos.json
# Não faz busca nenhuma: só conta com o mapa.
import json, math, sys, random
C = json.load(open(sys.argv[1])); GEO, OUT = sys.argv[2], sys.argv[3]
F = [f for f in json.load(open(GEO))['features'] if f['properties']['nome'] != 'MUNICIPIO']
def rings(g): return [g['coordinates'][0]] if g['type'] == 'Polygon' else [p[0] for p in g['coordinates']]
R = [r for f in F for r in rings(f['geometry'])]
P = [p for r in R for p in r]
lo0, lo1 = min(p[0] for p in P), max(p[0] for p in P); la0, la1 = min(p[1] for p in P), max(p[1] for p in P)
k = math.cos(math.radians((la0 + la1) / 2))
xy = lambda p: (p[0] * 111.32 * k, p[1] * 110.574)
def inside(p, r):
    c = False; lon, lat = p
    for (x1, y1), (x2, y2) in zip(r, r[1:] + r[:1]):
        if (y1 > lat) != (y2 > lat) and lon < (x2 - x1) * (lat - y1) / (y2 - y1) + x1: c = not c
    return c
def dseg(p, a, b):
    (px, py), (ax, ay), (bx, by) = xy(p), xy(a), xy(b); dx, dy = bx - ax, by - ay; L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L)); return math.hypot(px - ax - t * dx, py - ay - t * dy)
def dist_area(p):
    if any(inside(p, r) for r in R): return 0
    return min(dseg(p, a, b) for r in R for a, b in zip(r, r[1:] + r[:1]))
# amostra de pontos da área, para medir a cobertura
random.seed(1); A = []
while len(A) < 3000:
    p = (random.uniform(lo0, lo1), random.uniform(la0, la1))
    if dist_area(p) == 0: A.append(p)
def grid(s, ox, oy, borda):
    dlo = s / (111.32 * k); dla = s / 110.574; out = []; la = la0 + oy * dla
    while la < la1 + dla:
        lo = lo0 + ox * dlo
        while lo < lo1 + dlo:
            if dist_area((lo, la)) <= borda: out.append((lo, la))
            lo += dlo
        la += dla
    return out
def cobre(pts, raio): return sum(1 for a in A if min(math.dist(xy(a), xy(p)) for p in pts) <= raio) / len(A)
# grade dos termos densos: testa 16 deslocamentos e fica com a que cobre mais com menos pontos
s = C['grade_km']; best = None
for ox in (0, .25, .5, .75):
    for oy in (0, .25, .5, .75):
        g = grid(s, ox, oy, C['borda_km']); key = (-cobre(g, s * .75), len(g))
        if best is None or key < best[0]: best = (key, g)
g = best[1]
# pontos dos termos raros: k-means sobre a área; ponto que cair fora é puxado para dentro
n = C['pontos_raros']; Cn = random.sample(A, n)
for _ in range(50):
    G = [[] for _ in Cn]
    for a in A: G[min(range(n), key=lambda i: math.dist(xy(a), xy(Cn[i])))].append(a)
    Cn = [(sum(p[0] for p in g_) / len(g_), sum(p[1] for p in g_) / len(g_)) for g_ in G]
Cn = [c if dist_area(c) == 0 else min(A, key=lambda a: math.dist(xy(a), xy(c))) for c in Cn]
print(f'caixa da área: {(lo1 - lo0) * 111.32 * k:.1f} x {(la1 - la0) * 110.574:.1f} km')
print(f'termos densos: {len(g)} pontos (grade de {s} km); área a até {s * .75:.1f} km de um ponto: {100 * cobre(g, s * .75):.1f}%')
print(f'termos raros: {len(Cn)} pontos; maior distância até um ponto: {max(min(math.dist(xy(a), xy(c)) for c in Cn) for a in A):.2f} km')
nd, nr = len(C['termos_densos']), len(C['termos_raros'])
print(f'buscas da página 1: {nd} x {len(g)} + {nr} x {len(Cn)} = {nd * len(g) + nr * len(Cn)}')
json.dump({'densos': [(round(la, 4), round(lo, 4)) for lo, la in g], 'raros': [(round(la, 4), round(lo, 4)) for lo, la in Cn]}, open(OUT, 'w'))
