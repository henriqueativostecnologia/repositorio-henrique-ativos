# Passo 6: página para o celular (mapa, filtros e cartões com alertas e botões "Ver no Maps").
# Lojas visitadas: ficam em cinza com ✓ (pela planilha, passo 4, ou pelo botão "Marcar visitada", salvo no aparelho).
# Uso: python3 6_pagina.py dados/roteiro.json dados/Roteiro_CIDADE_DATA.html --leaflet dados/leaflet
# Tem dados reais: o arquivo gerado nunca entra no repositório.
# Funciona offline, aberta como arquivo no celular: o Leaflet vai embutido (pasta com leaflet.js e leaflet.css da versão 1.9.4)
# e o fundo do mapa é uma imagem embutida (fundo_mapa e limites_fundo na configuração; ver LEIA-ME, "gerar o fundo do mapa").
# Sem fundo_mapa na configuração, a página usa os quadradinhos do OpenStreetMap, que só carregam com a página publicada na internet.
import json, sys, html, math, base64, os, argparse, re
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
    D.append(dict(p=l['parada'], b=l['bloco'], n=l['nome'], s=l['seg'], ba=l['bairro'], br=l['bairro'].replace(' (borda)', ''), g=l['grupo2'], pl=1 if l['plan'] else 0,
                  sd=1 if l['sem_dono'] else 0, nt=l['nota'], av=l['aval'], al=l['alertas'], sit=l['sit'], w=l['site'], wc=canal(l['site']),
                  t=l['tel'], e=l['end'], m=l['link'], la=l['gps']['latitude'], lo=l['gps']['longitude'],
                  id=l['pid'], vr=(l.get('visita') or {}).get('r', ''), vd=(l.get('visita') or {}).get('d', ''),
                  ce=l.get('cenario', ''), si=l.get('sinais', ''), of=l.get('oferta', ''), cs=l.get('case', '')))
ROT = [dict(k=r['k'], nome=r['nome'], links=r['links'], km=round(r['km'], 1), n=r['n'], nop=r['nop']) for r in R['rotas']]
segs = sorted({d['s'] for d in D})
from collections import Counter as _C
bairros = [b for b, _ in _C(d['br'] for d in D).most_common()]
npl = sum(d['pl'] for d in D)
page = '''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Roteiro __TITULO__</title>
<style>__LEAFLET_CSS__</style>
<style>
:root{--vis:#7B3FA8;--bg:#F3F5F2;--papel:#fff;--tinta:#1D2B27;--suave:#5A6B66;--linha:#D3DCD8;--com:#2B5F8A;--sem:#2F7A4F;--op:#9AA19E;--alerta-bg:#FFF4DE;--alerta:#7A4B00;--sd:#C2662D}
@media (prefers-color-scheme:dark){:root{--vis:#C79BEA;--bg:#141B19;--papel:#1C2522;--tinta:#E6EEEA;--suave:#9AACA6;--linha:#33423D;--com:#7DB3E0;--sem:#72C495;--op:#6E7774;--alerta-bg:#3A2E14;--alerta:#F2C979;--sd:#E8955E;color-scheme:dark}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--tinta);font:15px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
header{background:var(--tinta);color:var(--bg);padding:16px max(16px,env(safe-area-inset-right)) 14px max(16px,env(safe-area-inset-left))}
header h1{margin:0;font-size:1.3rem}header p{margin:4px 0 0;font-size:.85rem;opacity:.8}
main{max-width:1400px;margin:0 auto;padding:0 max(16px,env(safe-area-inset-right)) 48px max(16px,env(safe-area-inset-left))}
.layout{display:grid;gap:16px}.col-lista{min-width:0;max-width:720px}
@media (min-width:900px){.layout{grid-template-columns:minmax(0,1.25fr) minmax(360px,1fr)}.col-mapa{position:sticky;top:58px;align-self:start}#mapa{height:calc(100vh - 110px)!important}}
.barra{position:sticky;top:0;z-index:1000;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--linha);display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.barra .resumo{flex-basis:100%;font-size:.8rem}@media (min-width:900px){.barra .resumo{flex-basis:auto}}
.barra .abre{border:1px solid var(--tinta);background:var(--tinta);color:var(--bg);border-radius:999px;padding:7px 14px;font:700 .88rem system-ui,sans-serif;cursor:pointer;min-height:36px}
.bloco-sel{display:inline-flex;align-items:center;gap:6px;font:700 .88rem system-ui,sans-serif}.bloco-sel select{font:600 .9rem system-ui,sans-serif;padding:7px 8px;border:1px solid var(--tinta);border-radius:999px;background:var(--papel);color:var(--tinta);min-height:36px;max-width:34vw}
@media (max-width:899px){.bloco-sel .rot{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}.barra{gap:6px}.bloco-sel select{font-size:.82rem;padding:7px 4px}.barra .abre{padding:7px 11px}}
#painel{padding:10px 0;border-bottom:1px solid var(--linha);max-height:60vh;overflow:auto}#painel .titulo{font-size:.78rem;font-weight:700;color:var(--suave);margin:6px 0 4px;text-transform:uppercase;letter-spacing:.04em}
.linha{display:flex;gap:6px;overflow-x:auto;padding-bottom:6px;scrollbar-width:none}.linha::-webkit-scrollbar{display:none}
@media (min-width:700px),(pointer:fine){.linha{flex-wrap:wrap;overflow-x:visible}}
.chip{flex:none;border:1px solid var(--linha);background:var(--papel);color:var(--tinta);border-radius:999px;padding:7px 12px;font:600 .85rem system-ui,sans-serif;min-height:36px;cursor:pointer;white-space:nowrap}
.chip[aria-pressed="true"]{background:var(--tinta);color:var(--bg);border-color:var(--tinta)}
.chip i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px;vertical-align:0}
.resumo{font-size:.82rem;color:var(--suave)}
#mapa{height:55vh;min-height:320px;border:1px solid var(--linha);border-radius:12px;margin-top:12px;background:var(--linha)}
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
.pin{width:24px;height:24px;border-radius:50%;color:#fff;display:grid;place-items:center;font:700 10px system-ui,sans-serif;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.4)}
.pin.sd{outline:2px solid var(--sd);outline-offset:1px}.pin.op{width:18px;height:18px;font-size:8px;opacity:.85}
.casa{background:#1D2B27;color:#fff;border-radius:6px;padding:2px 6px;font:700 11px system-ui,sans-serif;white-space:nowrap;border:2px solid #fff}
article.vis{opacity:.8;border-left:5px solid var(--vis)}article.vis h3::after{content:" ✓";color:var(--vis)}.visita .selo{color:var(--vis)!important}
.visita{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:10px;padding-top:10px;border-top:1px dashed var(--linha)}
.visita select{font:inherit;padding:7px;border:1px solid var(--linha);border-radius:8px;background:var(--papel);color:var(--tinta);flex:1 1 160px;min-height:38px}
.visita .marcar{border:1px solid var(--sem);color:var(--sem);background:transparent;padding:8px 12px;border-radius:8px;font:600 .88rem system-ui,sans-serif;cursor:pointer;min-height:38px}
.visita .selo{font-size:.82rem;font-weight:700;color:var(--sem)}
.pin.vis{background:var(--vis)!important;opacity:1;position:relative}.pin.vis::after{content:"✓";position:absolute;top:-6px;right:-6px;background:#fff;color:var(--vis);border-radius:50%;width:14px;height:14px;font-size:9px;display:grid;place-items:center}
#copiado{white-space:pre-wrap;font:12px ui-monospace,monospace;background:var(--papel);border:1px solid var(--linha);border-radius:8px;padding:8px;margin-top:8px;max-height:160px;overflow:auto}
.oferta{margin:8px 0 0;font-size:.88rem}.oferta .cen{display:inline-block;font-weight:700;font-size:.78rem;border-radius:6px;padding:1px 7px;background:var(--tinta);color:var(--bg);margin-right:4px}.oferta a{color:var(--com);font-weight:600}
section.bloco{scroll-margin-top:70px}
#vazio{display:none}button:focus-visible,a:focus-visible{outline:3px solid var(--sd);outline-offset:2px}
</style></head><body>
<header><h1>Roteiro de visitas · __TITULO__</h1><p>__NPL__ planejadas · __NOP__ opcionais · __NB__ blocos · saída: __SAIDA__</p></header>
<main>
<div class="barra"><label class="bloco-sel"><span class="rot">Grupo</span> <select id="gr" aria-label="Grupo"><option value="todos">Com/sem site</option><option value="com site">Com site</option><option value="sem site">Sem site</option></select></label><label class="bloco-sel"><span class="rot">Bloco</span> <select id="bl" aria-label="Mostrar só um bloco">__BLOPT__</select></label><button type="button" class="abre" id="abre" aria-expanded="false" aria-controls="painel">Filtros <span id="nf"></span></button><span class="resumo">Mostrando <b id="tot"></b> lojas · <b id="nvis">0</b> de __NPL__ planejadas visitadas</span></div>
<div id="painel" hidden>
<div class="titulo">Mostrar</div>
 <div class="linha" role="group" aria-label="Mostrar"><button class="chip" id="sd" aria-pressed="false"><i style="background:var(--sd)"></i>Só ficha sem dono</button><button class="chip" id="op" aria-pressed="true">Mostrar opcionais</button><button class="chip" id="ev" aria-pressed="false">Esconder visitadas</button><button class="chip" id="cp" type="button">Copiar visitas</button></div>
<div class="titulo">Segmentos (toque em mais de um para juntar)</div>
 <div class="linha" role="group" aria-label="Segmento"><button class="chip" data-sg="" aria-pressed="true">Todos os segmentos</button>__SEGS__</div>
<div class="titulo">Bairros (toque em mais de um para juntar)</div>
 <div class="linha" role="group" aria-label="Bairro"><button class="chip" data-br="" aria-pressed="true">Todos os bairros</button>__BAIRROS__</div>
<div id="copiado" hidden></div>
</div>
<div class="layout"><div class="col-mapa"><div id="mapa" role="region" aria-label="Mapa das paradas"></div>
<div class="leg"><span><i style="background:var(--vis)"></i>Visitada ✓</span><span><i style="background:var(--com)"></i>Com site</span><span><i style="background:var(--sem)"></i>Sem site</span><span><i style="background:var(--op)"></i>Opcional</span><span><i style="background:transparent;outline:3px solid var(--sd)"></i>Ficha sem dono</span></div></div><div class="col-lista">
<div class="dica"><b>Como usar:</b> visite todas as planejadas na ordem dos números. As opcionais (cinza, ex.: 12a) ficam perto da parada de mesmo número: entre se der tempo. Depois de cada visita, toque em <b>Marcar visitada</b> no cartão (fica salvo neste aparelho) e preencha a coluna "Resultado" na planilha, que é o registro oficial. A loja visitada não some: fica em cinza com ✓. "Copiar visitas" copia a lista para você colar na planilha ou mandar para o Claude.</div>
<p id="vazio" class="dica">Nenhuma loja com esses filtros. Toque em "Todos".</p>
__BLOCOS__
</div></div>
<p class="meta" style="margin-top:20px">Fonte: __FONTE__. Distâncias em linha reta; de carro o caminho é maior. Mapa © colaboradores do OpenStreetMap.</p>
</main>
<script>__LEAFLET_JS__</script>
<script>
const D=__DADOS__, O=__O__;
const st={gr:'todos',sg:new Set(),br:new Set(),sd:false,op:true,ev:false,bl:0};
const CHAVE='ativos-visitas-'+document.title;
let VL={}; try{VL=JSON.parse(localStorage.getItem(CHAVE)||'{}')||{}}catch(e){VL={}}
function salvar(){try{localStorage.setItem(CHAVE,JSON.stringify(VL))}catch(e){}}
function visita(d){const x=VL[d.id]; if(x) return x; return d.vr?{r:d.vr,d:d.vd,planilha:1}:null}
let map=null, mk={}, linha=null;
try{
 map=L.map('mapa',{tap:true}).setView(O,14);
 __FUNDO__
 L.marker(O,{icon:L.divIcon({className:'',html:'<div class="casa">Saída</div>',iconSize:[50,20],iconAnchor:[25,10]})}).addTo(map);
 linha=L.polyline([],{color:'#1D2B27',weight:2,opacity:.45,dashArray:'5 6'}).addTo(map);
 D.forEach(d=>{
  const cls=d.pl?(d.g==='com site'?'com':'sem'):'op';
  const cor=getComputedStyle(document.documentElement).getPropertyValue('--'+cls);
  d.cor=cor; const m=L.marker([d.la,d.lo],{icon:icone(d)});
  m.bindPopup(`<b>${d.p}. ${esc(d.n)}</b><br>${esc(d.s)} · ${d.g}<br><a href="${d.m}" target="_blank" rel="noopener">Ver no Maps</a> · <a href="#c${d.p}">Ver cartão</a>`);
  mk[d.p]=m;
 });
}catch(e){ map=null; document.getElementById('mapa').innerHTML='<p class="dica" style="margin:12px">O mapa precisa de internet para carregar. Os cartões abaixo funcionam sem ele.</p>'; }
function icone(d){return L.divIcon({className:'',html:`<div class="pin ${d.pl?'':'op'} ${d.sd?'sd':''} ${visita(d)?'vis':''}" style="background:${d.cor}">${d.p}</div>`,iconSize:d.pl?[24,24]:[18,18],iconAnchor:d.pl?[12,12]:[9,9]})}
function esc(t){return String(t).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function vis(d){return (st.gr==='todos'||d.g===st.gr)&&(st.sg.size===0||st.sg.has(d.s))&&(st.br.size===0||st.br.has(d.br))&&(!st.sd||d.sd)&&(st.op||d.pl)&&!(st.ev&&visita(d))&&(!st.bl||d.b===st.bl)}
function pintar(d){const v=visita(d), el=document.getElementById('c'+d.p); el.classList.toggle('vis',!!v);
 const s=el.querySelector('.selo'), b=el.querySelector('.marcar'), sel=el.querySelector('select');
 s.textContent=v?('✓ Visitada'+(v.d?' em '+v.d:'')+(v.planilha?' (planilha)':'')):''; b.textContent=v?(v.planilha?'Registrada na planilha':'Desmarcar'):'Marcar visitada'; b.disabled=!!(v&&v.planilha); sel.value=v?(v.r||''):sel.value;
 if(map&&mk[d.p]) mk[d.p].setIcon(icone(d));}
function aplicar(){
 const pts=[O]; let n=0;
 D.forEach(d=>{const v=vis(d); document.getElementById('c'+d.p).hidden=!v; n+=v;
  if(map){ if(v){mk[d.p].addTo(map); if(d.pl) pts.push([d.la,d.lo]);} else map.removeLayer(mk[d.p]); }});
 document.querySelectorAll('section.bloco').forEach(s=>{s.hidden=!s.querySelector('article:not([hidden])')});
 document.getElementById('tot').textContent=n; document.getElementById('nvis').textContent=D.filter(d=>d.pl&&visita(d)).length; document.getElementById('vazio').style.display=n?'none':'block';
 if(map){ linha.setLatLngs(pts); const b=D.filter(vis).map(d=>[d.la,d.lo]).concat([O]); if(b.length>1) map.fitBounds(b,{padding:[20,20],maxZoom:15}); }
 document.getElementById('gr').value=st.gr;
 document.querySelectorAll('[data-sg]').forEach(c=>c.setAttribute('aria-pressed',c.dataset.sg===''?st.sg.size===0:st.sg.has(c.dataset.sg)));
 document.querySelectorAll('[data-br]').forEach(c=>c.setAttribute('aria-pressed',c.dataset.br===''?st.br.size===0:st.br.has(c.dataset.br)));
 const nf=(st.sg.size>0?st.sg.size:0)+st.br.size+st.sd+(!st.op)+st.ev; document.getElementById('nf').textContent=nf?'('+nf+')':'';
 document.getElementById('sd').setAttribute('aria-pressed',st.sd); document.getElementById('op').setAttribute('aria-pressed',st.op); document.getElementById('ev').setAttribute('aria-pressed',st.ev);
}
document.getElementById('gr').onchange=e=>{st.gr=e.target.value;aplicar()};
document.querySelectorAll('[data-sg]').forEach(c=>c.onclick=()=>{const s=c.dataset.sg; if(!s) st.sg.clear(); else st.sg.has(s)?st.sg.delete(s):st.sg.add(s); aplicar()});
document.querySelectorAll('[data-br]').forEach(c=>c.onclick=()=>{const s=c.dataset.br; if(!s) st.br.clear(); else st.br.has(s)?st.br.delete(s):st.br.add(s); aplicar()});
document.getElementById('sd').onclick=()=>{st.sd=!st.sd;aplicar()};
document.getElementById('op').onclick=()=>{st.op=!st.op;aplicar()};
document.getElementById('ev').onclick=()=>{st.ev=!st.ev;aplicar()};
document.getElementById('bl').onchange=e=>{st.bl=+e.target.value; aplicar(); if(st.bl&&matchMedia('(min-width:900px)').matches){const s=document.getElementById('b'+st.bl); if(s) s.scrollIntoView({block:'start'})}};
const ab=document.getElementById('abre'), pn=document.getElementById('painel');
ab.onclick=()=>{pn.hidden=!pn.hidden; ab.setAttribute('aria-expanded',!pn.hidden)};
addEventListener('resize',()=>{ if(map) map.invalidateSize() });
const hoje=()=>new Date().toLocaleDateString('pt-BR');
D.forEach(d=>{const el=document.getElementById('c'+d.p), b=el.querySelector('.marcar'), sel=el.querySelector('select');
 b.onclick=()=>{ if(VL[d.id]) delete VL[d.id]; else if(!d.vr) VL[d.id]={r:sel.value,d:hoje()}; else return; salvar(); pintar(d); aplicar(); };
 sel.onchange=()=>{ if(VL[d.id]){VL[d.id].r=sel.value;} else if(sel.value){VL[d.id]={r:sel.value,d:hoje()};} salvar(); pintar(d); aplicar(); };
 pintar(d);});
document.getElementById('cp').onclick=()=>{
 const linhas=D.filter(d=>VL[d.id]).map(d=>[d.p,d.n,VL[d.id].r||'(sem resultado)',VL[d.id].d,d.m].join(' | '));
 const txt=linhas.length?('Parada | Loja | Resultado | Data | Link do Maps\\n'+linhas.join('\\n')):'Nenhuma visita marcada neste aparelho.';
 const box=document.getElementById('copiado'); box.hidden=false; box.textContent=txt;
 const ok=()=>{box.textContent='Copiado ('+linhas.length+' visitas). Cole na planilha ou mande para o Claude.\\n\\n'+txt};
 try{navigator.clipboard.writeText(txt).then(ok,()=>{})}catch(e){}
 const r=document.createRange(); r.selectNodeContents(box); const s=getSelection(); s.removeAllRanges(); s.addRange(r);};
document.querySelectorAll('.vermapa').forEach(b=>b.onclick=()=>{ if(!map) return; const m=mk[b.dataset.p]; document.getElementById('mapa').scrollIntoView({behavior:'smooth',block:'center'}); setTimeout(()=>{map.setView(m.getLatLng(),17);m.openPopup()},350)});
aplicar();
</script></body></html>'''
RES = ['Não falei com quem decide', 'Sem interesse', 'Talvez', 'Interessado', 'Fechou']
OPCOES = '<option value="">Resultado…</option>' + ''.join(f'<option>{E(x)}</option>' for x in RES)
def oferta_html(d):
    if not d['ce']: return ''
    m = re.search(r'https?://\S+', d['cs'] or ''); nome = (d['cs'] or '').split(' - http')[0].strip()
    case = (f'<a href="{E(m.group(0))}" target="_blank" rel="noopener">{E(nome)}</a>' if m else E(nome)) if d['cs'] else ''
    return (f'<div class="oferta"><span class="cen">Cenário {E(d["ce"])}</span> {E(d["of"])}'
            + (f'<br><span class="meta">Sinais: {E(d["si"])}</span>' if d['si'] else '')
            + (f'<br><span class="meta">Case a levar: {case}</span>' if case else '') + '</div>')
cards = []
for r in ROT:
    bl = [d for d in D if d['b'] == r['k']]
    links = ''.join(f'<a class="rota" href="{E(u)}" target="_blank" rel="noopener">Abrir rota do bloco no Maps (a partir de onde você está)</a>' for i, u in enumerate(r['links']))
    cards.append(f'<section class="bloco" id="b{r["k"]}"><h2>{E(r["nome"])}</h2><p class="meta">{r["n"]} planejadas · {r["nop"]} opcionais · cerca de {fmt(r["km"])} km em linha reta</p>{links}')
    for d in bl:
        cls = ('com' if d['g'] == 'com site' else 'sem') if d['pl'] else 'op'
        nota = f'nota {fmt(d["nt"])} ({mil(d["av"] or 0)} aval.)' if d['nt'] is not None else 'sem nota'
        al = ''.join(f'<li>{E(a)}</li>' for a in d['al'])
        canal = f'<a href="{E(d["w"])}" target="_blank" rel="noopener">{E(d["wc"])}</a>' if d['w'] else ''
        cards.append(f'''<article id="c{E(d["p"])}" class="{'op' if not d['pl'] else ''}"><div class="top"><span class="n {cls}">{E(d["p"])}</span><div><h3>{E(d["n"])}{' <span class="tag">opcional</span>' if not d['pl'] else ''}</h3>
<p class="meta">{E(d["s"])} · {E(d["ba"])} · {nota}</p><p class="meta">{'Com site' if d['g'] == 'com site' else 'Sem site'} ({E(d["sit"])})</p>{f'<p class="meta">Tel.: <span class="tel">{E(d["t"])}</span></p>' if d['t'] else ''}</div></div>
{oferta_html(d)}{f'<ul class="alertas">{al}</ul>' if al else ''}<div class="btns"><a href="{E(d["m"])}" target="_blank" rel="noopener">Ver no Maps</a>{canal}<button type="button" class="vermapa" data-p="{E(d["p"])}">No mapa</button></div>
<div class="visita"><button type="button" class="marcar">Marcar visitada</button><select aria-label="Resultado da visita">{OPCOES}</select><span class="selo"></span></div></article>''')
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
page = (page.replace('__TITULO__', E(CF['titulo'])).replace('__SAIDA__', E(CF['ponto_saida']['nome'])).replace('__FONTE__', E(CF['fonte'])).replace('__NPL__', str(npl)).replace('__NOP__', str(len(D) - npl)).replace('__NB__', str(len(ROT))).replace('__SEGS__', segchips).replace('__BAIRROS__', ''.join(f'<button class="chip" data-br="{E(b)}" aria-pressed="false">{E(b)}</button>' for b in bairros)).replace('__BLOPT__', '<option value="0">Blocos: todos</option>' + ''.join(f'<option value="{r["k"]}">{E(r["nome"])}</option>' for r in ROT))
        .replace('__BLOCOS__', '\n'.join(cards)).replace('__DADOS__', json.dumps(D, ensure_ascii=False)).replace('__O__', json.dumps(list(O))))
page = page.replace('__FUNDO__', fundo)
page = page.replace('__LEAFLET_CSS__', open(os.path.join(a.leaflet, 'leaflet.css')).read()).replace('__LEAFLET_JS__', open(os.path.join(a.leaflet, 'leaflet.js')).read())
open(OUT, 'w').write(page); print('ok', len(D), len(page) // 1024, 'KB')
