# Passo 3: junta as respostas guardadas, separa por segmento e marca grupo (com site / sem site), ficha sem dono, rede e gourmet.
# Uso: python3 3_classificar.py dados/config.json dados/ dados/bairros.geojson dados/lojas.json
# Não faz busca: lê só o que está em dados/raw/.
import json, glob, sys, re, math, unicodedata
from collections import Counter, defaultdict
C = json.load(open(sys.argv[1])); D, GEO, OUT = sys.argv[2], sys.argv[3], sys.argv[4]

def norm(s): return re.sub(r'\s+', ' ', unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()).strip()

# bairros
F = [f for f in json.load(open(GEO))['features'] if f['properties']['nome'] != 'MUNICIPIO']
def rings(g): return [g['coordinates'][0]] if g['type'] == 'Polygon' else [p[0] for p in g['coordinates']]
BR = [(f['properties']['nome'], rings(f['geometry'])) for f in F]
def inside(lon, lat, r):
    c = False
    for (x1, y1), (x2, y2) in zip(r, r[1:] + r[:1]):
        if (y1 > lat) != (y2 > lat) and lon < (x2 - x1) * (lat - y1) / (y2 - y1) + x1: c = not c
    return c
def bairro(r):
    g = r.get('gps_coordinates') or {}
    lat, lon = g.get('latitude'), g.get('longitude')
    if lat is not None:
        for n, rs in BR:
            if any(inside(lon, lat, x) for x in rs): return n
    a = norm(r.get('address')); cid = norm(C['cidade_no_endereco'])
    for b in C['bairros_sem_contorno']:  # bairro da área sem contorno no mapa: vale o endereço
        if norm(b) in a and cid in a: return b
    if lat is not None and cid in a:  # borda: até borda_km de um bairro da área, com endereço na cidade
        d, n = min((dseg((lon, lat), p, q), n) for n, rs in BR for x in rs for p, q in zip(x, x[1:] + x[:1]))
        if d <= C['borda_km']: return n + ' (borda)'
    return None
_lat = [p[1] for _, rs in BR for x in rs for p in x]
K = math.cos(math.radians((min(_lat) + max(_lat)) / 2))
def dseg(p, a, b):
    xy = lambda v: (v[0] * 111.32 * K, v[1] * 110.574)
    (px, py), (ax, ay), (bx, by) = xy(p), xy(a), xy(b); dx, dy = bx - ax, by - ay; L2 = dx * dx + dy * dy
    t = 0 if L2 == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L2)); return math.hypot(px - ax - t * dx, py - ay - t * dy)

# site
SOCIAL = {'instagram.com': 'só Instagram', 'facebook.com': 'só Facebook', 'fb.com': 'só Facebook', 'linktr.ee': 'só Linktree',
          'wa.me': 'só WhatsApp', 'whatsapp': 'só WhatsApp', 'ifood.com': 'só iFood', 'beacons.ai': 'só página de links',
          'linkbio': 'só página de links', 'bio.site': 'só página de links', 'ola.click': 'só cardápio online',
          'anota.ai': 'só cardápio online', 'goomer': 'só cardápio online', 'cardapio': 'só cardápio online',
          'g.page': 'só link da ficha do Google', 'g.co/': 'só link da ficha do Google', 'business.site': 'só site grátis do Google',
          'bit.ly': 'link encurtado', 'tinyurl': 'link encurtado', 'jusbrasil': 'só perfil no Jusbrasil', 'olx.com': 'só anúncio na OLX',
          'webmotors': 'só anúncio em portal', 'icarros': 'só anúncio em portal', 'mercadolivre': 'só anúncio em portal'}
def site(w):
    wl = (w or '').lower()
    if not wl: return 'Sem site', 'sem site'
    for k, v in SOCIAL.items():
        if k in wl: return 'Sem site', v
    return 'Com site', 'site próprio'

# carregar
DENSOS, RAROS = C['termos_densos'], C['termos_raros']
L = {}; cheias = Counter(); buscas = Counter(); erros = []
for f in glob.glob(f'{D}/raw/*.json'):
    d = json.load(open(f)); p = d.get('search_parameters', {}); q = p.get('q')
    if q not in DENSOS + RAROS: continue
    if 'error' in d or '_err' in d: erros.append((q, p.get('ll'), d.get('error') or d.get('_err'))); continue
    start = int(p.get('start') or 0); lr = d.get('local_results') or []
    buscas[q] += 1; cheias[q] += len(lr) >= 20
    for i, r in enumerate(lr):
        p_ = r.get('position') or i + 1
        pos = p_ if p_ > start else start + p_  # na página 2 a posição pode vir 1–20 ou 21–40
        x = L.setdefault(r['place_id'], dict(r=r, qs=set(), pos=pos))
        x['qs'].add(q); x['pos'] = min(x['pos'], pos)

# segmento
AUTO = ('automotiv', 'carro', 'auto ', 'autos', 'veicul', 'car ', 'car studio', 'detail', 'lava', 'motor', 'moto')
EST = ('estetica', 'detalhamento', 'detailing', 'polimento', 'vitrificacao', 'car studio', 'ppf', 'insulfilm', 'pelicula', 'envelopamento', 'higienizacao')
def segmento(x):
    r = x['r']; t = norm(' '.join([r.get('title', ''), r.get('type') or '', ' '.join(r.get('types') or [])])); qs = x['qs']
    tp = norm(r.get('type'))
    if qs & {'advocacia previdenciária', 'advocacia trabalhista'} and ('advog' in t or 'advocacia' in t or 'juridic' in t):
        if {'advocacia previdenciária', 'advocacia trabalhista'} <= qs: return 'Advocacia (trabalhista e previdenciária)', ''
        return ('Advocacia previdenciária' if 'advocacia previdenciária' in qs else 'Advocacia trabalhista'), ''
    if qs & {'estética automotiva', 'detalhamento automotivo'}:
        auto = any(k in t + ' ' for k in AUTO); est = any(k in t for k in EST)
        if est and auto: return 'Estética / detalhamento', ''
        if auto and 'lava' not in t: return 'Estética / detalhamento', 'conferir'
        if auto and 'lava' in t and 'lava-rápido' not in qs: return 'Estética / detalhamento', 'conferir'
    if 'lava-rápido' in qs and ('lava' in t or 'lavagem' in t):
        return 'Lava-jato', ''
    if 'compra e venda de veículos' in qs and any(k in t for k in ('carro', 'veicul', 'automov', 'concession', 'revend', 'seminov', 'moto')): return 'Compra e venda de veículos', ''
    if 'construtora' in qs and ('constru' in t or 'empreiteir' in t or 'incorpor' in t): return 'Construtora', ''
    if 'imobiliária' in qs and ('imobil' in t or 'imove' in t or 'corretor' in t): return 'Imobiliária', ''
    if 'cafeteria' in qs and ('cafe' in t or 'coffee' in t or 'cafeteria' in t or 'espresso' in t): return 'Cafeteria', ''
    if 'empório' in qs and any(k in t for k in ('empori', 'mercearia', 'armazem', 'produtos naturais', 'gourmet', 'delicat', 'queij', 'organic')): return 'Empório', ''
    if 'bar' in qs and any(k in t for k in ('bar', 'pub', 'boteco', 'botequim', 'choperia', 'cervej', 'petisc')): return 'Bar', ''
    if 'restaurante' in qs and any(k in t for k in ('restaurante', 'churrasc', 'pizzaria', 'comida', 'lanchonete', 'hamburg', 'self', 'bistro', 'cozinha', 'sushi', 'japon', 'grill', 'galeteria', 'marmit')): return 'Restaurante', ''
    return None, ''

FORTE = ('especial', 'specialty', 'coffee', 'torrefa', 'barista', 'graos', 'espresso', 'coado', 'v60', 'metodos', 'artesanal', 'cafe gourmet', 'gourmet')
TIPO_CAFE = ('loja de cafe', 'torrefacao', 'espresso bar')
NAO_CAFE = ('padaria', 'lanchonete', 'confeitaria', 'doceria', 'restaurante', 'sorveteria', 'loja de conveniencia', 'mercado', 'supermercado', 'acai')
def gourmet(r):
    nome = norm(r.get('title')); tp = norm(r.get('type')); tps = norm(' '.join(r.get('types') or []))
    desc = norm(json.dumps(r.get('extensions') or [], ensure_ascii=False) + ' ' + (r.get('description') or ''))
    if any(k in nome for k in FORTE) or any(k in tp or k in tps for k in TIPO_CAFE) or any(k in desc for k in ('cafe especial', 'cafes especiais', 'specialty', 'torrefa', 'barista', 'metodos')):
        return 'Sim'
    if any(tp.startswith(k) for k in NAO_CAFE): return 'Não'
    return 'Conferir'

REDES = tuple(norm(x) for x in C['redes'])  # nomes de redes/franquias (em dados/config.json, fora do repositório)
GEN = {'restaurante', 'bar', 'lava', 'jato', 'rapido', 'imobiliaria', 'cafeteria', 'cafe', 'emporio', 'advocacia', 'advogados', 'advogado', 'construtora',
       'estetica', 'automotiva', 'e', 'de', 'do', 'da', 'dos', 'das', 'o', 'a', 'centro', 'pizzaria', 'lanchonete', 'veiculos', 'automoveis', 'car'} | set(norm(C['cidade_no_endereco']).split())
def marca(t): return ' '.join([w for w in re.split(r'[^a-z0-9]+', norm(re.split(r'[-|–(]', t)[0])) if w and w not in GEN][:2])

linhas = []; fora = Counter(); lava_fora = 0
for pid, x in L.items():
    r = x['r']; b = bairro(r)
    if not b: fora['fora da área'] += 1; continue
    s, obs = segmento(x)
    if not s: fora['não é do segmento'] += 1; continue
    LJ = C['lava_jato_minimo']
    if s == 'Lava-jato' and not ((r.get('rating') or 0) >= LJ['nota'] and (r.get('reviews') or 0) >= LJ['avaliacoes']): lava_fora += 1; continue
    g, sit = site(r.get('website'))
    linhas.append(dict(pid=pid, nome=r['title'], seg=s, obs=obs, bairro=b, grupo=g, sit=sit, site=r.get('website'), tel=r.get('phone'),
                       end=r.get('address'), nota=r.get('rating'), aval=r.get('reviews'), tipo=r.get('type'), tipos=r.get('types'),
                       sem_dono='Sim' if r.get('unclaimed_listing') else '', pos=x['pos'], qs=sorted(x['qs']),
                       gourmet=gourmet(r) if s == 'Cafeteria' else '', gps=r.get('gps_coordinates'),
                       rede='', link=f"https://www.google.com/maps/place/?q=place_id:{pid}"))
for l in linhas:
    nn = norm(l['nome']) + ' ' + norm(l['site'])
    if any(k in nn for k in REDES): l['rede'] = 'Sim'
    l['marca'] = marca(l['nome'])
json.dump(dict(linhas=linhas, fora=fora, lava_fora=lava_fora, cheias=cheias, buscas=buscas, erros=erros), open(OUT, 'w'), ensure_ascii=False, default=list)

# resumo (só contagens, sem nomes)
print('buscas por termo:', dict(buscas)); print('páginas cheias (20 de 20) por termo:', dict(cheias)); print('erros:', erros)
print('lojas únicas:', len(L), '| fora:', dict(fora), '| lava-jato abaixo do mínimo:', lava_fora, '| na planilha:', len(linhas))
T = defaultdict(Counter)
for l in linhas:
    t = T[l['seg']]; t['total'] += 1; t[l['grupo']] += 1; t['sem dono'] += bool(l['sem_dono']); t['rede'] += bool(l['rede'])
for k, t in sorted(T.items()): print(k, dict(t))
print('bairros:', Counter(l['bairro'] for l in linhas).most_common())
print('situação do site:', Counter(l['sit'] for l in linhas).most_common())
