# Passo 2: faz as buscas no Google Maps pela SerpApi (servidor MCP), um termo por busca.
# Uso:
#   python3 2_buscar.py dados/config.json dados/ dados/pontos.json --simular            (só conta, não gasta busca)
#   python3 2_buscar.py dados/config.json dados/ dados/pontos.json                      (página 1 de todos os termos)
#   python3 2_buscar.py dados/config.json dados/ dados/pontos.json --pagina 2 --termos "imobiliária,construtora"
# A chave da SerpApi NÃO está aqui: no ambiente do Claude ela entra pela rede.
# Cada resposta fica em dados/raw/ (busca repetida não é cobrada de novo) e em dados/calls.log.
# Trava: para quando as buscas usadas no mês chegarem a limite_mes - trava (contador em dados/contador.json).
import json, sys, os, hashlib, urllib.request, argparse
ap = argparse.ArgumentParser(); ap.add_argument('config'); ap.add_argument('dados'); ap.add_argument('pontos')
ap.add_argument('--pagina', type=int, default=1); ap.add_argument('--termos', default=''); ap.add_argument('--simular', action='store_true')
a = ap.parse_args()
C = json.load(open(a.config)); D = a.dados; PTS = json.load(open(a.pontos))
os.makedirs(f'{D}/raw', exist_ok=True)
CNT = f'{D}/contador.json'
cnt = json.load(open(CNT)) if os.path.exists(CNT) else {'usadas': 0}
def arquivo(params): return f"{D}/raw/{hashlib.md5(json.dumps(params, sort_keys=True).encode()).hexdigest()}.json"
def search(params):
    f = arquivo(params)
    if os.path.exists(f): return json.load(open(f)), False
    if cnt['usadas'] >= C['limite_mes'] - C['trava']:
        print('TRAVA: faltam', C['limite_mes'] - cnt['usadas'], 'buscas no mês. Parando.'); sys.exit(2)
    body = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "search", "arguments": {"params": params}}}
    req = urllib.request.Request("https://mcp.serpapi.com/mcp", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
    r = urllib.request.urlopen(req, timeout=120).read().decode()
    if r.startswith("event:") or "data:" in r[:20]: r = [l[5:] for l in r.splitlines() if l.startswith("data:")][-1]
    j = json.loads(r); cnt['usadas'] += 1; json.dump(cnt, open(CNT, 'w'))
    with open(f'{D}/calls.log', 'a') as L: L.write(json.dumps(params, ensure_ascii=False) + "\n")
    res = j.get("result", {}); txt = res.get("content", [{}])[0].get("text", "") if res.get("content") else ""
    try: data = json.loads(txt)
    except Exception: data = {"_raw": txt[:2000], "_err": j.get("error")}
    json.dump(data, open(f, "w"), ensure_ascii=False); return data, True
so = [t.strip() for t in a.termos.split(',') if t.strip()]
plano = [(q, p, C['zoom_densos']) for q in C['termos_densos'] for p in PTS['densos']] + \
        [(q, p, C['zoom_raros']) for q in C['termos_raros'] for p in PTS['raros']]
if so: plano = [x for x in plano if x[0] in so]
def params(q, la, lo, z):
    p = dict(engine='google_maps', type='search', q=q, ll=f'@{la},{lo},{z}z', hl='pt-br', gl='br')
    if a.pagina > 1: p['start'] = 20 * (a.pagina - 1)
    return p
if a.simular:
    novas = sum(1 for q, (la, lo), z in plano if not os.path.exists(arquivo(params(q, la, lo, z))))
    print(f'plano: {len(plano)} buscas | já guardadas: {len(plano) - novas} | novas (gastam saldo): {novas} | usadas no mês: {cnt["usadas"]}')
    sys.exit(0)
feitas = 0
for q, (la, lo), z in plano:
    d, nova = search(params(q, la, lo, z)); feitas += nova; lr = d.get('local_results') or []
    print(q, f'| pág. {a.pagina} |', la, lo, '|', len(lr), 'lojas |', d.get('error', '') or d.get('_err', '') or '', '| nova' if nova else '| guardada', flush=True)
print('buscas novas:', feitas, '| usadas no mês:', cnt['usadas'], '| plano:', len(plano))
