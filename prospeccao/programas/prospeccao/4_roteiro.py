# Passo 4: separa planejadas e opcionais, monta os blocos de visita e os alertas de cada loja.
# Uso: python3 4_roteiro.py dados/config.json dados/lojas.json dados/roteiro.json [dados/visitas.xlsx]
# Planejada = cenários A, B e C (e "B ou C" / "B ou D" até o teste do site). Opcional = só o cenário D (presas à planejada mais próxima: 12a, 12b...).
# Cenário A-D, sinais, oferta e case a levar: regras de 16/11/2026 (limites na configuração, campo "cenario").
# Blocos de até 10 planejadas, do mais perto para o mais longe do ponto de saída.
import json, math, sys, re, string, unicodedata, os
from collections import Counter, defaultdict
C = json.load(open(sys.argv[1])); J = json.load(open(sys.argv[2])); OUT = sys.argv[3]
# Opcional: 4º argumento = planilha de visitas (aba Lojas, .xlsx ou .csv). As visitas já registradas
# (Resultado, data, com quem falou, objeção, próximo passo) voltam para as mesmas lojas, pelo "Link do Maps".
VIS = {}
if len(sys.argv) > 4:
    f = sys.argv[4]
    if f.lower().endswith('.csv'):
        import csv
        rows = list(csv.reader(open(f, encoding='utf-8-sig')))
    else:
        import openpyxl
        wb_ = openpyxl.load_workbook(f, read_only=True, data_only=True)
        rows = [list(r) for r in (wb_['Lojas'] if 'Lojas' in wb_.sheetnames else wb_.active).iter_rows(values_only=True)]
    h = {str(x).strip(): i for i, x in enumerate(rows[0]) if x}
    campos = {'r': 'Resultado', 'd': 'Data da visita', 'quem': 'Falou com quem', 'obj': 'Objeção', 'prox': 'Próximo passo'}
    for r in rows[1:]:
        lk = r[h['Link do Maps']] if 'Link do Maps' in h and h['Link do Maps'] < len(r) else None
        v = {k: (str(r[h[c]]).strip() if c in h and h[c] < len(r) and r[h[c]] not in (None, '') else '') for k, c in campos.items()}
        if lk and any(v.values()): VIS[str(lk).strip()] = v
O = (C['ponto_saida']['lat'], C['ponto_saida']['lon'])
def km(a, b):
    R = 6371.0088; p1, p2 = math.radians(a[0]), math.radians(b[0]); dp = p2 - p1; dl = math.radians(b[1] - a[1])
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2; return 2 * R * math.asin(math.sqrt(h))
def norm(s): return unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()

FORA = [norm(x) for x in C['fora_do_roteiro']]; CONF = [norm(x) for x in C['conferir_segmento']]
L = [l for l in J['linhas'] if not any(x in norm(l['nome']) for x in FORA)]
# segmentos só para mapear (ainda não abordar): ficam fora do roteiro, numa aba própria da planilha
SM = set(C.get('so_mapear', [])); SO_MAPEAR = [l for l in L if l['seg'] in SM]; L = [l for l in L if l['seg'] not in SM]
# ---- Cenário A-D (regras de 16/11/2026) ----
# A = sem site próprio; B = site próprio que falha em 1+ teste (sem HTTPS, não se adapta ao celular, PageSpeed no celular
# abaixo do limite, fora do ar; ano antigo no rodapé só como apoio); C = site ok e Google fraco; D = o resto.
# Os testes do site vêm de um arquivo (campo "testes_sites" da configuração): {url: {https, celular, pagespeed, fora_do_ar, ano}}.
CE = C.get('cenario', {}); LIM_NOTA = CE.get('nota_minima', 4.0); LIM_AV = CE.get('avaliacoes_minimas', 10)
LIM_PS = CE.get('pagespeed_minimo', 50); LIM_ANO = CE.get('ano_antigo', 2023)
TS = {}
if C.get('testes_sites') and os.path.exists(C['testes_sites']): TS = json.load(open(C['testes_sites']))
OFERTA = {'A': 'Google Meu Negócio + site novo', 'B': 'Google Meu Negócio + reforma do site',
          'C': 'Google Meu Negócio (+ ajuste leve no site)', 'D': 'Baixa prioridade (outro serviço ou diagnóstico de cortesia)',
          'B ou C': 'Google Meu Negócio (+ site: reforma ou ajuste leve, ver no teste)', 'B ou D': 'Definir depois do teste do site'}
CASES = C.get('cases', {})
def fmtn(v): return format(v, '.1f').replace('.', ',')
for l in L:
    g = []  # sinais do Google
    if l['nota'] is not None and l['nota'] < LIM_NOTA: g.append(f"nota {fmtn(l['nota'])} com {l['aval'] or 0} avaliações")
    if (l['aval'] or 0) < LIM_AV: g.append('sem avaliações' if not l['aval'] else f"só {l['aval']} avaliações")
    if l['sem_dono']: g.append('ficha sem dono')
    if l.get('horario') is False: g.append('sem horário na ficha')
    if l['sit'] != 'site próprio':
        cen, s = 'A', [l['sit']] + g
    else:
        t_ = TS.get(l['site'])
        if not t_:  # sem o teste do site não dá para separar B de C/D; os dois casos ficam planejados até o teste
            cen, s = ('B ou C' if g else 'B ou D'), ['site não testado'] + g
        else:
            f = []
            if t_.get('fora_do_ar'): f.append('site fora do ar')
            else:
                if t_.get('https') is False: f.append('sem HTTPS')
                if t_.get('celular') is False: f.append('não se adapta ao celular')
                if t_.get('pagespeed') is not None and t_['pagespeed'] < LIM_PS: f.append(f"PageSpeed no celular {t_['pagespeed']}")
            if f:
                if t_.get('ano') and t_['ano'] <= LIM_ANO: f.append(f"rodapé de {t_['ano']}")
                cen, s = 'B', f + g
            elif g: cen, s = 'C', g
            else: cen, s = 'D', []
    l['cenario'] = cen; l['sinais'] = '; '.join(s); l['oferta'] = OFERTA[cen]
    l['case'] = CASES.get(l['seg'], '')
print('cenários:', dict(Counter(l['cenario'] for l in L)), '| sites testados:', len(TS))
for l in L:
    l['p'] = (l['gps']['latitude'], l['gps']['longitude'])
    # regra de 16/11/2026: planejada = 10+ avaliações (com qualquer nota) ou ficha sem dono; opcional = menos de 10 avaliações
    # regra de 16/11/2026: só o cenário D (site ok e Google ok) é opcional; poucas avaliações também é bom alvo
    l['plan'] = l['cenario'] != 'D'
    l['grupo2'] = 'com site' if l['grupo'] == 'Com site' else 'sem site'
    l['dup_de'] = None
# mesma marca: a de melhor avaliação fica normal; as outras recebem o alerta
chave = lambda l: (-(l['nota'] or 0), -(l['aval'] or 0))
M = defaultdict(list)
for l in L:
    if not l['rede'] and l['marca']: M[(l['seg'], l['marca'])].append(l)
for v in M.values():
    if len(v) > 1:
        v.sort(key=chave)
        for x in v[1:]: x['dup_de'] = v[0]

# blocos: semente = planejada livre mais perto da avenida; o bloco cresce pela vizinha mais próxima do bloco
P = [l for l in L if l['plan']]; livres = P[:]; blocos = []
while livres:
    s = min(livres, key=lambda l: km(O, l['p'])); b = [s]; livres.remove(s)
    while len(b) < 10 and livres:
        n = min(livres, key=lambda l: min(km(l['p'], x['p']) for x in b)); b.append(n); livres.remove(n)
    blocos.append(b)
# ordem dentro do bloco: vizinho mais próximo a partir do fim do bloco anterior + 2-opt (caminho aberto)
def caminho(ini, pts):
    rest = pts[:]; r = []; cur = ini
    while rest:
        n = min(rest, key=lambda l: km(cur, l['p'])); r.append(n); rest.remove(n); cur = n['p']
    tot = lambda r: km(ini, r[0]['p']) + sum(km(r[i]['p'], r[i + 1]['p']) for i in range(len(r) - 1))
    mel = True
    while mel:
        mel = False
        for i in range(len(r) - 1):
            for j in range(i + 1, len(r)):
                nr = r[:i] + r[i:j + 1][::-1] + r[j + 1:]
                if tot(nr) < tot(r) - 1e-9: r = nr; mel = True
    return r
cur = O; n = 0; rotas = []
for k, b in enumerate(blocos, 1):
    b[:] = caminho(cur, b); ini = cur
    for x in b:
        n += 1; x['parada'] = str(n); x['bloco'] = k; x['dist'] = km(cur, x['p']); cur = x['p']
    rotas.append((k, ini, [x['p'] for x in b]))
# opcionais: presas à planejada mais próxima, com letra
op = defaultdict(list)
for l in L:
    if not l['plan']:
        a = min(P, key=lambda x: km(x['p'], l['p'])); op[a['parada']].append(l); l['ancora'] = a
for pid, v in op.items():
    a = v[0]['ancora']; v.sort(key=lambda l: km(a['p'], l['p']))
    for i, l in enumerate(v):
        l['parada'] = f"{pid}{string.ascii_lowercase[i]}"; l['bloco'] = a['bloco']; l['dist'] = km(a['p'], l['p'])
# bairros dos blocos
def nome_bloco(k):
    c = Counter(re.sub(r' \(borda\)', '', x['bairro']) for x in blocos[k - 1]).most_common(2)
    return f"Bloco {k}: " + ' e '.join(b for b, _ in c)
for l in L: l['bloco_nome'] = nome_bloco(l['bloco'])
# alertas
for l in L:
    a = []
    if l['sem_dono']: a.append('Ficha sem dono: mostrar no celular')
    if (l['aval'] or 0) < 10: a.append('Poucas avaliações: confirme que está aberta')
    if l['nota'] is not None and l['nota'] < 4.0: a.append('Nota baixa: conversa sobre reputação')
    if l['rede']: a.append('Rede: perguntar quem decide o marketing')
    if any(x in norm(l['nome']) for x in CONF): a.append('Conferir se é do segmento')
    if l['dup_de']: a.append(f"Conferir se é a mesma loja da parada {l['dup_de']['parada']}")
    if l['obs'] == 'conferir': a.append('Conferir se é do segmento (estética/detalhamento)')
    l['alertas'] = a
# faixas para o resumo
def fnota(v): return 'sem nota' if v is None else ('abaixo de 4,0' if v < 4 else ('4,0 a 4,4' if v < 4.5 else '4,5 a 5,0'))
def faval(v): v = v or 0; return 'menos de 10' if v < 10 else ('10 a 49' if v < 50 else ('50 a 199' if v < 200 else '200 ou mais'))
for l in L: l['fnota'] = fnota(l['nota']); l['faval'] = faval(l['aval'])
def ordem(p): m = re.match(r'(\d+)([a-z]?)', p); return (int(m.group(1)), m.group(2))
L.sort(key=lambda l: ordem(l['parada']))
# links de rota no Google Maps: até 10 pontos por link
LINKS = []
for k, ini, pts in rotas:
    # origem vazia = "Seu local" no celular; o Google Maps aceita até 10 paradas, e o bloco tem no máximo 10
    partes = ['https://www.google.com/maps/dir//' + '/'.join(f'{a:.6f},{b:.6f}' for a, b in pts)]
    LINKS.append(dict(k=k, nome=nome_bloco(k), links=partes, km=km(ini, pts[0]) + sum(km(pts[i], pts[i + 1]) for i in range(len(pts) - 1)), n=len(pts),
                      nop=sum(len(op[x['parada']]) for x in blocos[k - 1])))
for l in L:
    for k in ('ancora', 'dup_de'): l.pop(k, None)
for l in L: l['visita'] = VIS.get(l['link'], {})
json.dump(dict(L=L, O=O, rotas=LINKS, config=C, so_mapear=SO_MAPEAR), open(OUT, 'w'), ensure_ascii=False)
print('só mapear (fora do roteiro):', len(SO_MAPEAR))
print('visitas trazidas da planilha:', sum(1 for l in L if l['visita']), 'de', len(VIS))
print('lojas', len(L), '| planejadas', len(P), '| opcionais', len(L) - len(P), '| blocos', len(blocos), [len(b) for b in blocos])
print(Counter((l['grupo2'], l['plan']) for l in L))
for r in LINKS: print(r['nome'], '|', r['n'], 'planejadas +', r['nop'], 'opcionais |', round(r['km'], 1), 'km |', round(km(O, blocos[r['k'] - 1][0]['p']), 2), 'km da avenida até a 1ª parada')
print('alertas', Counter(a for l in L for a in l['alertas']))
