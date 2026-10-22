# Passo 6: página para o celular (mapa, filtros e cartões com alertas e botões "Ver no Maps").
# Uso: python3 6_pagina.py dados/roteiro.json dados/Roteiro_CIDADE_DATA.html --leaflet dados/leaflet
# Tem dados reais: o arquivo gerado nunca entra no repositório.
# Funciona offline, aberta como arquivo no celular: o Leaflet vai embutido (pasta com leaflet.js e leaflet.css da versão 1.9.4)
# e o fundo do mapa é uma imagem embutida (fundo_mapa e limites_fundo na configuração; ver LEIA-ME, "gerar o fundo do mapa").
# Sem fundo_mapa na configuração, a página usa os quadradinhos do OpenStreetMap, que só carregam com a página publicada na internet.
import json, sys, html, math, base64, os, argparse
ap = argparse.ArgumentParser(); ap.add_argument('roteiro'); ap.add_argument('saida'); ap.add_argument('--leaflet', required=True, help='pasta com leaflet.js e leaflet.css (Leaflet 1.9.4)')
a = ap.parse_args(); sys.argv = [sys.argv[0], a.roteiro, a.saida]
R = json.load(open(sys.argv[1])); L = R['L']; O = R['O']; OUT = sys.argv[2]; CF = R['config']
E = html.escape
def fmt(v): return format(v, '.1f').replace('.', ',')
def mil(v): return format(v, ',').replace(',', '.')
def canal(u):
    if not u: return None
    ul = u.lower()
    if 'instagram.com' in ul: return 'Instagram'
    if 'facebook.com' in ul or 'fb.com' in ul: return 'Facebook'
    if 'wa.me' in ul or 'whatsapp' in ul: return 'WhatsApp'
    if 'ifood' in ul: return 'iFood'
    return 'Site'
D = []
for l in L:
    D.append(dict(p=l['parada'], b=l['bloco'], n=l['nome'], s=l['seg'], ba=l['bairro'], g=l['grupo2'], pl=1 if l['plan'] else 0,
                  sd=1 if l['sem_dono'] else 0, nt=l['nota'], av=l['aval'], al=l['alertas'], sit=l['sit'], w=l['site'], wc=canal(l['site']),
                  t=l['tel'], e=l['end'], m=l['link'], la=l['gps']['latitude'], lo=l['gps']['longitude']))
ROT = [dict(k=r['k'], nome=r['nome'], links=r['links'], km=round(r['km'], 1), n=r['n'], nop=r['nop']) for r in R['rotas']]
segs = sorted({d['s'] for d in D})
npl = sum(d['pl'] for d in D)
page = '''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Roteiro __TITULO__</title>
<style>__LEAFLET_CSS__</style>
<style>
:root{--bg:#F3F5F2;--papel:#fff;--tinta:#1D2B27;--suave:#5A6B66;--linha:#D3DCD8;--com:#2B5F8A;--sem:#2F7A4F;--op:#9AA19E;--alerta-bg:#FFF4DE;--alerta:#7A4B00;--sd:#C2662D}
@media (prefers-color-scheme:dark){:root{--bg:#141B19;--papel:#1C2522;--tinta:#E6EEEA;--suave:#9AACA6;--linha:#33423D;--com:#7DB3E0;--sem:#72C495;--op:#6E7774;--alerta-bg:#3A2E14;--alerta:#F2C979;--sd:#E8955E;color-scheme:dark}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--tinta);font:15px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
header{background:var(--tinta);color:var(--bg);padding:16px max(16px,env(safe-area-inset-right)) 14px max(16px,env(safe-area-inset-left))}
header h1{margin:0;font-size:1.3rem}header p{margin:4px 0 0;font-size:.85rem;opacity:.8}
main{max-width:680px;margin:0 auto;padding:0 max(16px,env(safe-area-inset-right)) 48px max(16px,env(safe-area-inset-left))}
.filtros{position:sticky;top:0;z-index:1000;background:var(--bg);padding:10px 0 8px;border-bottom:1px solid var(--linha)}
.linha{display:flex;gap:6px;overflow-x:auto;padding-bottom:6px;scrollbar-width:none}.linha::-webkit-scrollbar{display:none}
.chip{flex:none;border:1px solid var(--linha);background:var(--papel);color:var(--tinta);border-radius:999px;padding:7px 12px;font:600 .85rem system-ui,sans-serif;min-height:36px;cursor:pointer;white-space:nowrap}
.chip[aria-pressed="true"]{background:var(--tinta);color:var(--bg);border-color:var(--tinta)}
.chip i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px;vertical-align:0}
.resumo{font-size:.82rem;color:var(--suave)}
#mapa{height:330px;border:1px solid var(--linha);border-radius:12px;margin-top:12px;background:var(--linha)}
.leg{display:flex;flex-wrap:wrap;gap:12px;font-size:.8rem;color:var(--suave);margin-top:6px}.leg span{display:inline-flex;align-items:center;gap:5px}
.leg i{width:12px;height:12px;border-radius:50%;display:inline-block}
.dica{background:var(--papel);border-left:4px solid var(--com);border-radius:8px;padding:10px 12px;margin-top:12px;font-size:.9rem}
h2{font-size:1.05rem;margin:26px 0 2px}.meta{margin:2px 0 0;color:var(--suave);font-size:.83rem}
.rota{display:inline-block;background:var(--com);color:#fff;padding:9px 12px;border-radius:9px;text-decoration:none;font-weight:700;font-size:.88rem;margin:8px 6px 8px 0}
article{background:var(--papel);border:1px solid var(--linha);border-radius:12px;padding:12px 14px;margin-bottom:9px;scroll-margin-top:130px}
article.op{background:transparent;border-style:dashed;color:var(--suave)}
.top{display:flex;gap:10px;align-items:flex-start}.n{flex:none;min-width:30px;height:30px;padding:0 6px;border-radius:15px;color:#fff;display:grid;place-items:center;font-weight:700;font-size:.82rem}
.n.com{background:var(--com)}.n.sem{background:var(--sem)}.n.op{background:var(--op)}
h3{margin:0;font-size:1rem;color:var(--tinta)}.tag{display:inline-block;font-size:.72rem;font-weight:700;border-radius:999px;padding:1px 7px;margin-left:4px;vertical-align:1px;border:1px solid currentColor}
.alertas{margin:8px 0 0;padding:8px 10px;background:var(--alerta-bg);color:var(--alerta);border-radius:8px;font-size:.86rem;font-weight:600;list-style:none}
.alertas li+li{margin-top:3px}.tel{user-select:all;font-variant-numeric:tabular-nums}
.btns{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}.btns a,.btns button{flex:1 1 30%;text-align:center;border:1px solid var(--com);color:var(--com);background:transparent;padding:9px 4px;border-radius:8px;text-decoration:none;font:600 .88rem system-ui,sans-serif;cursor:pointer}
.pin{width:28px;height:28px;border-radius:50%;color:#fff;display:grid;place-items:center;font:700 10px system-ui,sans-serif;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.4)}
.pin.sd{outline:3px solid var(--sd);outline-offset:1px}.pin.op{width:20px;height:20px;font-size:8px;opacity:.9}
.casa{background:#1D2B27;color:#fff;border-radius:6px;padding:2px 6px;font:700 11px system-ui,sans-serif;white-space:nowrap;border:2px solid #fff}
#vazio{display:none}button:focus-visible,a:focus-visible{outline:3px solid var(--sd);outline-offset:2px}
</style></head><body>
<header><h1>Roteiro de visitas · __TITULO__</h1><p>__NPL__ planejadas · __NOP__ opcionais · __NB__ blocos · saída: __SAIDA__</p></header>
<main>
<div class="filtros">
 <div class="linha" role="group" aria-label="Grupo"><button class="chip" data-gr="todos" aria-pressed="true">Todos</button><button class="chip" data-gr="com site" aria-pressed="false"><i style="background:var(--com)"></i>Com site</button><button class="chip" data-gr="sem site" aria-pressed="false"><i style="background:var(--sem)"></i>Sem site</button><button class="chip" id="sd" aria-pressed="false"><i style="background:var(--sd)"></i>Só ficha sem dono</button><button class="chip" id="op" aria-pressed="true">Mostrar opcionais</button></div>
 <div class="linha" role="group" aria-label="Segmento"><button class="chip" data-sg="" aria-pressed="true">Todos os segmentos</button>__SEGS__</div>
 <div class="resumo">Mostrando <b id="tot"></b> lojas. Toque em mais de um segmento para juntar.</div>
</div>
<div id="mapa" role="region" aria-label="Mapa das paradas"></div>
<div class="leg"><span><i style="background:var(--com)"></i>Com site</span><span><i style="background:var(--sem)"></i>Sem site</span><span><i style="background:var(--op)"></i>Opcional</span><span><i style="background:transparent;outline:3px solid var(--sd)"></i>Ficha sem dono</span></div>
<div class="dica"><b>Como usar:</b> visite todas as planejadas na ordem dos números. As opcionais (cinza, ex.: 12a) ficam perto da parada de mesmo número: entre se der tempo. Depois de cada visita, preencha a coluna "Resultado" na planilha.</div>
<p id="vazio" class="dica">Nenhuma loja com esses filtros. Toque em "Todos".</p>
__BLOCOS__
<p class="meta" style="margin-top:20px">Fonte: __FONTE__. Distâncias em linha reta; de carro o caminho é maior. Mapa © colaboradores do OpenStreetMap.</p>
</main>
<script>__LEAFLET_JS__</script>
<script>
const D=__DADOS__, O=__O__;
const st={gr:'todos',sg:new Set(),sd:false,op:true};
let map=null, mk={}, linha=null;
try{
 map=L.map('mapa',{tap:true}).setView(O,14);
 __FUNDO__
 L.marker(O,{icon:L.divIcon({className:'',html:'<div class="casa">Saída</div>',iconSize:[50,20],iconAnchor:[25,10]})}).addTo(map);
 linha=L.polyline([],{color:'#1D2B27',weight:2,opacity:.45,dashArray:'5 6'}).addTo(map);
 D.forEach(d=>{
  const cls=d.pl?(d.g==='com site'?'com':'sem'):'op';
  const cor=getComputedStyle(document.documentElement).getPropertyValue('--'+cls);
  const m=L.marker([d.la,d.lo],{icon:L.divIcon({className:'',html:`<div class="pin ${d.pl?'':'op'} ${d.sd?'sd':''}" style="background:${cor}">${d.p}</div>`,iconSize:d.pl?[28,28]:[20,20],iconAnchor:d.pl?[14,14]:[10,10]})});
  m.bindPopup(`<b>${d.p}. ${esc(d.n)}</b><br>${esc(d.s)} · ${d.g}<br><a href="${d.m}" target="_blank" rel="noopener">Ver no Maps</a> · <a href="#c${d.p}">Ver cartão</a>`);
  mk[d.p]=m;
 });
}catch(e){ map=null; document.getElementById('mapa').innerHTML='<p class="dica" style="margin:12px">O mapa precisa de internet para carregar. Os cartões abaixo funcionam sem ele.</p>'; }
function esc(t){return String(t).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function vis(d){return (st.gr==='todos'||d.g===st.gr)&&(st.sg.size===0||st.sg.has(d.s))&&(!st.sd||d.sd)&&(st.op||d.pl)}
function aplicar(){
 const pts=[O]; let n=0;
 D.forEach(d=>{const v=vis(d); document.getElementById('c'+d.p).hidden=!v; n+=v;
  if(map){ if(v){mk[d.p].addTo(map); if(d.pl) pts.push([d.la,d.lo]);} else map.removeLayer(mk[d.p]); }});
 document.querySelectorAll('section.bloco').forEach(s=>{s.hidden=!s.querySelector('article:not([hidden])')});
 document.getElementById('tot').textContent=n; document.getElementById('vazio').style.display=n?'none':'block';
 if(map){ linha.setLatLngs(pts); const b=D.filter(vis).map(d=>[d.la,d.lo]).concat([O]); if(b.length>1) map.fitBounds(b,{padding:[20,20]}); }
 document.querySelectorAll('[data-gr]').forEach(c=>c.setAttribute('aria-pressed',c.dataset.gr===st.gr));
 document.querySelectorAll('[data-sg]').forEach(c=>c.setAttribute('aria-pressed',c.dataset.sg===''?st.sg.size===0:st.sg.has(c.dataset.sg)));
 document.getElementById('sd').setAttribute('aria-pressed',st.sd); document.getElementById('op').setAttribute('aria-pressed',st.op);
}
document.querySelectorAll('[data-gr]').forEach(c=>c.onclick=()=>{st.gr=c.dataset.gr;aplicar()});
document.querySelectorAll('[data-sg]').forEach(c=>c.onclick=()=>{const s=c.dataset.sg; if(!s) st.sg.clear(); else st.sg.has(s)?st.sg.delete(s):st.sg.add(s); aplicar()});
document.getElementById('sd').onclick=()=>{st.sd=!st.sd;aplicar()};
document.getElementById('op').onclick=()=>{st.op=!st.op;aplicar()};
document.querySelectorAll('.vermapa').forEach(b=>b.onclick=()=>{ if(!map) return; const m=mk[b.dataset.p]; document.getElementById('mapa').scrollIntoView({behavior:'smooth',block:'center'}); setTimeout(()=>{map.setView(m.getLatLng(),17);m.openPopup()},350)});
aplicar();
</script></body></html>'''
cards = []
for r in ROT:
    bl = [d for d in D if d['b'] == r['k']]
    links = ''.join(f'<a class="rota" href="{E(u)}" target="_blank" rel="noopener">Abrir rota do bloco no Maps (a partir de onde você está)</a>' for i, u in enumerate(r['links']))
    cards.append(f'<section class="bloco"><h2>{E(r["nome"])}</h2><p class="meta">{r["n"]} planejadas · {r["nop"]} opcionais · cerca de {fmt(r["km"])} km em linha reta</p>{links}')
    for d in bl:
        cls = ('com' if d['g'] == 'com site' else 'sem') if d['pl'] else 'op'
        nota = f'nota {fmt(d["nt"])} ({mil(d["av"] or 0)} aval.)' if d['nt'] is not None else 'sem nota'
        al = ''.join(f'<li>{E(a)}</li>' for a in d['al'])
        canal = f'<a href="{E(d["w"])}" target="_blank" rel="noopener">{E(d["wc"])}</a>' if d['w'] else ''
        cards.append(f'''<article id="c{E(d["p"])}" class="{'op' if not d['pl'] else ''}"><div class="top"><span class="n {cls}">{E(d["p"])}</span><div><h3>{E(d["n"])}{' <span class="tag">opcional</span>' if not d['pl'] else ''}</h3>
<p class="meta">{E(d["s"])} · {E(d["ba"])} · {nota}</p><p class="meta">{'Com site' if d['g'] == 'com site' else 'Sem site'} ({E(d["sit"])})</p>{f'<p class="meta">Tel.: <span class="tel">{E(d["t"])}</span></p>' if d['t'] else ''}</div></div>
{f'<ul class="alertas">{al}</ul>' if al else ''}<div class="btns"><a href="{E(d["m"])}" target="_blank" rel="noopener">Ver no Maps</a>{canal}<button type="button" class="vermapa" data-p="{E(d["p"])}">No mapa</button></div></article>''')
    cards.append('</section>')
segchips = ''.join(f'<button class="chip" data-sg="{E(s)}" aria-pressed="false">{E(s)}</button>' for s in segs)
if CF.get('fundo_mapa'):
    lim = CF['limites_fundo']; FB = [lim['sudoeste'], lim['nordeste']]
    ext = os.path.splitext(CF['fundo_mapa'])[1].lower().lstrip('.').replace('jpg', 'jpeg')
    img = base64.b64encode(open(CF['fundo_mapa'], 'rb').read()).decode()
    fundo = (f"const FB={json.dumps(FB)};L.imageOverlay('data:image/{ext};base64,{img}',FB,{{attribution:'&copy; colaboradores do OpenStreetMap'}}).addTo(map);"
             "map.setMaxBounds(FB);map.setMinZoom(13);map.setMaxZoom(16);")
else:
    fundo = "L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,attribution:'&copy; OpenStreetMap'}).addTo(map);"
page = (page.replace('__TITULO__', E(CF['titulo'])).replace('__SAIDA__', E(CF['ponto_saida']['nome'])).replace('__FONTE__', E(CF['fonte'])).replace('__NPL__', str(npl)).replace('__NOP__', str(len(D) - npl)).replace('__NB__', str(len(ROT))).replace('__SEGS__', segchips)
        .replace('__BLOCOS__', '\n'.join(cards)).replace('__DADOS__', json.dumps(D, ensure_ascii=False)).replace('__O__', json.dumps(list(O))))
page = page.replace('__FUNDO__', fundo)
page = page.replace('__LEAFLET_CSS__', open(os.path.join(a.leaflet, 'leaflet.css')).read()).replace('__LEAFLET_JS__', open(os.path.join(a.leaflet, 'leaflet.js')).read())
open(OUT, 'w').write(page); print('ok', len(D), len(page) // 1024, 'KB')
