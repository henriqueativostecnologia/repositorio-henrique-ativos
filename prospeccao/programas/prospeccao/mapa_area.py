# Mapa simples da área (só dados públicos: contornos do OpenStreetMap). Serve para aprovar a área antes da estimativa.
# Uso: python3 mapa_area.py dados/config.json dados/bairros.geojson dados/mapa_area.html mapa_area_modelo.html
import json, math, sys, html
C = json.load(open(sys.argv[1])); src, out = sys.argv[2], sys.argv[3]; sys.argv = sys.argv[:1] + sys.argv[2:]
F = json.load(open(src))['features']
mun = [f for f in F if f['properties']['nome'] == 'MUNICIPIO']
B = [f for f in F if f['properties']['nome'] != 'MUNICIPIO']

def rings(g):
    if g['type'] == 'Polygon': return [g['coordinates'][0]]
    if g['type'] == 'MultiPolygon': return [p[0] for p in g['coordinates']]
    return []
def area_km2(r, k):
    a = 0
    for (x1, y1), (x2, y2) in zip(r, r[1:] + r[:1]): a += x1 * y2 - x2 * y1
    return abs(a) / 2 * (111.320 * k) * 110.574
def centroid(r):
    a = cx = cy = 0
    for (x1, y1), (x2, y2) in zip(r, r[1:] + r[:1]):
        c = x1 * y2 - x2 * y1; a += c; cx += (x1 + x2) * c; cy += (y1 + y2) * c
    return (cx / (3 * a), cy / (3 * a)) if a else r[0]

pts = [p for f in B for r in rings(f['geometry']) for p in r]
lon0, lon1 = min(p[0] for p in pts), max(p[0] for p in pts)
lat0, lat1 = min(p[1] for p in pts), max(p[1] for p in pts)
pad = 0.006; lon0 -= pad; lon1 += pad; lat0 -= pad; lat1 += pad
k = math.cos(math.radians((lat0 + lat1) / 2))
W = 800; sc = W / ((lon1 - lon0) * k); H = round((lat1 - lat0) * sc)
P = lambda x, y: (round((x - lon0) * k * sc, 1), round((lat1 - y) * sc, 1))
path = lambda r: 'M' + 'L'.join('%s,%s' % P(*p) for p in r) + 'Z'

svg = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Mapa dos bairros da área de prospecção">']
svg.append('<defs><clipPath id="vista"><rect width="%d" height="%d"/></clipPath></defs><g clip-path="url(#vista)">' % (W, H))
for f in mun:
    for r in rings(f['geometry']): svg.append(f'<path class="mun" d="{path(r)}"/>')
rows = []
for f in sorted(B, key=lambda f: f['properties']['nome']):
    rs = rings(f['geometry']); nome = f['properties']['nome']
    big = max(rs, key=lambda r: area_km2(r, k))
    a = sum(area_km2(r, k) for r in rs); rows.append((nome, a))
    cls = 'b centro' if nome == 'Centro' else 'b'
    svg.append(f'<path class="{cls}" d="{" ".join(path(r) for r in rs)}"><title>{html.escape(nome)} · {a:.2f} km²</title></path>')
for f in B:
    nome = f['properties']['nome']; rs = rings(f['geometry'])
    x, y = P(*centroid(max(rs, key=lambda r: area_km2(r, k))))
    svg.append(f'<text x="{x}" y="{y}" class="lbl{" lc" if nome == "Centro" else ""}">{html.escape(nome)}</text>')
# barra de escala: 1 km
km = sc / (111.320 * k) * 1
svg.append(f'<g class="esc"><line x1="20" y1="{H-20}" x2="{20+km:.1f}" y2="{H-20}"/><text x="20" y="{H-28}">1 km</text></g>')
svg.append('<g class="norte"><text x="%d" y="34">N ↑</text></g>' % (W - 40))
svg.append('</g></svg>')
total = sum(a for _, a in rows)
lista = ''.join(f'<li><span>{html.escape(n)}</span><span class="num">{format(a,'.2f').replace('.',',')}</span></li>' for n, a in rows)
page = open(sys.argv[3]).read().replace('__SVG__', ''.join(svg)).replace('__LISTA__', lista) \
    .replace('__TOTAL__', f'{total:.1f}'.replace('.', ',')).replace('__N__', str(len(rows))) \
    .replace('__TITULO__', html.escape(C['titulo'])).replace('__AREA__', html.escape(C['area_descricao'])) \
    .replace('__SEM_CONTORNO__', ('<b>Sem contorno no mapa:</b> ' + html.escape(', '.join(C['bairros_sem_contorno'])) + '. Entram na busca pelos pontos vizinhos e pelo endereço. ') if C['bairros_sem_contorno'] else '')
open(out, 'w').write(page)
print(len(rows), round(total, 2), W, H)
