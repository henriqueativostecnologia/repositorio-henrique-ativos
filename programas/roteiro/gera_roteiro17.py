import json, math, re, html, urllib.parse, collections, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
SP='dados/'  # pasta com os arquivos de entrada e saída (fica FORA do repositório: dados reais)
X=SP+'xl/'
sel=json.load(open(X+'sel17.json'))
FORA={'Restaurante Exemplo da Instituição':'restaurante público: quem decide é a instituição','Rede Exemplo Seminovos':'rede nacional: o marketing é da matriz'}  # exemplos
fora=[s for s in sel if s['Nome'] in FORA]; sel=[s for s in sel if s['Nome'] not in FORA]
def km(a,b,c,d):
    R=6371.0088; p1,p2=math.radians(a),math.radians(c); dp=p2-p1; dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2; return 2*R*math.asin(math.sqrt(h))
# ponto de saída: estimado pelos km do Jaraguá da planilha (mínimos quadrados, busca em grade)
pts=[(a,b,c) for a,b,c in json.load(open(X+'pts.json')) if a and c is not None]
best=None
la0=sum(p[0] for p in pts)/len(pts); lo0=sum(p[1] for p in pts)/len(pts); step=0.02
for _ in range(6):
    cand=[(la0+i*step,lo0+j*step) for i in range(-10,11) for j in range(-10,11)]
    best=min(cand,key=lambda o:sum((km(o[0],o[1],a,b)-c)**2 for a,b,c in pts)); la0,lo0=best; step/=5
O=best; err=max(abs(km(O[0],O[1],a,b)-c) for a,b,c in pts)
P=[(s['Latitude'],s['Longitude']) for s in sel]
# rota: vizinho mais próximo a partir de casa + 2-opt (caminho aberto)
rest=list(range(len(sel))); rota=[]; cur=O
while rest:
    i=min(rest,key=lambda i:km(*cur,*P[i])); rota.append(i); rest.remove(i); cur=P[i]
def L(r): return km(*O,*P[r[0]])+sum(km(*P[r[i]],*P[r[i+1]]) for i in range(len(r)-1))
mel=True
while mel:
    mel=False
    for i in range(len(rota)-1):
        for j in range(i+1,len(rota)):
            nr=rota[:i]+rota[i:j+1][::-1]+rota[j+1:]
            if L(nr)<L(rota)-1e-9: rota=nr; mel=True
tot=L(rota)
# blocos de até 8 paradas
# blocos: corta nos maiores saltos entre lojas vizinhas (blocos de 4 a 10 paradas)
def partir(seq):
    if len(seq)<=10: return [seq]
    saltos=sorted(range(4,len(seq)-3),key=lambda j:-km(*P[seq[j-1]],*P[seq[j]]))
    j=saltos[0]; return partir(seq[:j])+partir(seq[j:])
cortes=[j for j in range(4,len(rota)-3) if km(*P[rota[j-1]],*P[rota[j]])>1.2]
B=[];ini=0
for j in cortes:
    if j-ini>=4: B.append(rota[ini:j]); ini=j
B.append(rota[ini:])
B=[x for blk in B for x in partir(blk)]
def nome_bloco(b,k):
    c=collections.Counter(sel[i]['Bairro'] for i in b).most_common(3)
    return f'{k}. '+', '.join(x for x,_ in c)
def fmt(v): return format(v,'.1f').replace('.',',')
def mil(v): return format(v,',').replace(',','.')
PITCH={'Restaurante':'página com cardápio, fotos e WhatsApp','Doceria':'página com cardápio de doces, encomendas pelo WhatsApp e fotos','Imobiliária':'página para captar proprietários e mostrar imóveis, com WhatsApp','Construtora':'página com obras entregues, fotos e WhatsApp','Revenda de seminovos':'página com o estoque e WhatsApp','Estética / detailing':'página com antes e depois; mostrar a demo do Lava Jato Exemplo'}
def pitch(seg): return 'página informativa sobre a área e contato (regras da OAB: sem promessa de resultado nem preço)' if seg.startswith('Advog') else PITCH.get(seg,'página própria com WhatsApp')
def situ(s):
    site=s['Site'] or ''; o=s['Observação'] or ''
    if s['Tem site? (Sim/Não)']=='Sim': return 'Tem site (ainda não avaliado: abra no celular antes)','Tem site'
    if 'Instagram' in o: return 'O "site" é só Instagram','Só Instagram'
    if 'Linktree' in o: return 'O "site" é só Linktree','Só Linktree'
    if 'Facebook' in o: return 'O "site" é só Facebook','Só Facebook'
    if 'WhatsApp' in o: return 'O "site" é só um link de WhatsApp','Só WhatsApp'
    return 'Sem site','Sem site'
def forte(s): return s['Ficha não assumida pelo dono']=='Sim' or (s['Melhor alvo']=='SIM' and s['Ativo (10+ aval.)']=='SIM')
def arg(s):
    a=[]
    if s['Ficha não assumida pelo dono']=='Sim': a.append('A ficha do Google NÃO foi assumida pelo dono: ofereça o diagnóstico do Google.')
    t,_=situ(s); nota=s['Nota']; av=s['Avaliações']
    a.append(f'{t}. Nota {fmt(nota)} com {mil(av)} avaliações.' if nota is not None else f'{t}. Sem nota no Google.')
    o=s['Observação'] or ''
    if 'nota 3' in o: a.append('Nota abaixo de 4,0: comece pelas avaliações (pedir e responder).')
    if 'franquia' in o: a.append('Franquia: peça para falar com o franqueado.')
    if 'menos de 10' in o: a.append('Poucas avaliações: pedir avaliação a cada cliente.')
    a.append('Proposta: '+pitch(s['Segmento'])+'.')
    return ' '.join(a)
def linkweb(u):
    if not u: return None
    from urllib.parse import urlparse
    q=urlparse(u); host=q.netloc.lower().replace('www.',''); path=q.path.strip('/')
    if 'instagram.com' in host:
        h=path.split('/')[0]; return ('Instagram','@'+h,f'https://www.instagram.com/{h}/')
    if 'linktr.ee' in host: return ('Linktree','linktr.ee/'+path.split('/')[0],f'https://linktr.ee/{path.split("/")[0]}')
    if 'facebook.com' in host: return ('Facebook',path.split('/')[0],u)
    if host=='wa.me': return ('WhatsApp','link do WhatsApp',u)
    if 'cardapioweb' in host: return ('Cardápio online',host,u)
    if 'appfranquiaexemplo' in host: return ('Encomendas online','app da franquia',u)  # exemplo
    if 'tinyurl' in host: return ('Link','link encurtado (abrir para ver)',u)
    clean=u.split('?')[0] if 'utm_' in u else u
    return ('Site',host,clean)
REDES=json.load(open(X+'redes.json'))
def canais(s):
    r=REDES.get(s['Nome'],{}); out=[]
    lk=linkweb(s['Site'])
    # site / página
    if r.get('site'): out.append(('Site',r['site'].split('//')[1].strip('/').replace('www.',''),r['site'],''))
    elif lk and lk[0] not in ('Instagram','WhatsApp'): out.append((lk[0],lk[1],lk[2],''))
    # instagram
    ig=r.get('ig') or (lk[1][1:] if lk and lk[0]=='Instagram' else None)
    if ig: out.append(('Instagram','@'+ig,f'https://www.instagram.com/{ig}/','achado na busca' if r.get('busca') else ''))
    # whatsapp
    if r.get('wa'): out.append(('WhatsApp',fmtel(r['wa']),'https://wa.me/'+r['wa'],''))
    elif r.get('wal'): out.append(('WhatsApp','link do WhatsApp',r['wal'],''))
    elif lk and lk[0]=='WhatsApp': out.append(('WhatsApp','link do Google',lk[2],''))
    else:
        dg=re.sub(r'\D','',s['Telefone'] or '')
        if len(dg)==11 and dg[2]=='9': out.append(('WhatsApp',fmtel('55'+dg),'https://wa.me/55'+dg,'celular do Google, confirmar'))
    return out,r.get('obs')
def planc(s):
    cs,ob=canais(s); g=lambda k:next((c[2] for c in cs if c[0]==k),'')
    site=next((c[2] for c in cs if c[0] not in ('Instagram','WhatsApp')),'')
    notas=[f"{c[0]}: {c[3]}" for c in cs if c[3]]+([ob] if ob else [])
    return [site,g('Instagram'),g('WhatsApp'),'; '.join(notas)]
def fmtel(w):
    d=w[2:] if w.startswith('55') else w
    return f'({d[:2]}) {d[2:-4]}-{d[-4:]}' if len(d)>=10 else w
def tel(t): return 'tel:+55'+re.sub(r'\D','',t) if t else None
def mdir(pts): return 'https://www.google.com/maps/dir/'+'/'.join(f'{a},{b}' for a,b in pts)
base=[nome_bloco(b,0)[3:] for b in B]; tot_n=collections.Counter(base); vis=collections.Counter()
def rot(k,b):
    x=base[k-1]; vis[x]+=1
    return f'{k}. {x}'+(f' (parte {vis[x]} de {tot_n[x]})' if tot_n[x]>1 else '')
linhas=[];rotas=[];prev=O;n=0
for k,b in enumerate(B,1):
    nb=rot(k,b); ptsb=[prev]+[P[i] for i in b]
    rotas.append((nb,mdir(ptsb),sum(km(*ptsb[j],*ptsb[j+1]) for j in range(len(ptsb)-1))))
    for i in b:
        n+=1; s=sel[i]; linhas.append((n,nb,s,arg(s),km(*(prev),*P[i]))); prev=P[i]
# planilha
wb=openpyxl.Workbook(); ws=wb.active; ws.title='Roteiro 16-10-v2'
cols=['Parada','Bloco','Alvo forte?','Setor','Segmento','Nome','Bairro','Endereço','Telefone','Nota','Avaliações','Situação do site','Site','Instagram','WhatsApp','Observação dos links','Ficha não assumida pelo dono','Km desde a parada anterior (linha reta)','Argumento','Link do Maps','Visitou? (S/N)','Falou com quem','Reação do dono','Objeção','Próximo passo']
ws.append(cols)
for n,b,s,a,d in linhas:
    ws.append([n,b,'Sim' if forte(s) else '',s['Setor'],s['Segmento'],s['Nome'],s['Bairro'],s['Endereço'],s['Telefone'] or '',s['Nota'],s['Avaliações'],situ(s)[1],*planc(s),s['Ficha não assumida pelo dono'] or '',round(d,2),a,s['Link do Maps'],None,None,None,None,None])
for c in ws[1]: c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor='172631'); c.alignment=Alignment(wrap_text=True)
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment=Alignment(wrap_text=True,vertical='top')
    row[9].number_format='0.0'; row[10].number_format='#,##0'
    if row[2].value=='Sim':
        for c in row[:3]: c.fill=PatternFill('solid',fgColor='E3F1E6')
for i,w in enumerate([7,24,8,11,16,30,14,34,16,6,10,14,30,30,26,30,10,10,56,28,10,16,30,30,24],1): ws.column_dimensions[get_column_letter(i)].width=w
ws.freeze_panes='G2'; ws.auto_filter.ref=ws.dimensions
wr=wb.create_sheet('Rotas no Maps'); wr.append(['Bloco','Km do bloco (linha reta)','Link da rota'])
for b,u,d in rotas: wr.append([b,round(d,2),u])
wr.column_dimensions['A'].width=50; wr.column_dimensions['C'].width=110
wf=wb.create_sheet('Fora do roteiro'); wf.append(['Nome','Motivo'])
for s in fora: wf.append([s['Nome'],FORA[s['Nome']]])
wf.column_dimensions['A'].width=50; wf.column_dimensions['B'].width=60
wb.save(SP+'Roteiro_visitas_16-10-v2.xlsx')
# página
E=html.escape; out=[]; cur=None
LF=open(SP+'lf/package/dist/leaflet.js').read(); LC=open(SP+'lf/package/dist/leaflet.css').read()
def grp(seg):
    if seg.startswith('Advog'): return 'Advocacia'
    return {'Revenda de seminovos':'Revenda de carros','Estética / detailing':'Estética automotiva'}.get(seg,seg)
CORES={'Restaurante':'#C2410C','Doceria':'#BE185D','Imobiliária':'#2A5A7E','Construtora':'#6D4C1F','Advocacia':'#5B21B6','Revenda de carros':'#0F766E','Estética automotiva':'#374151'}
nf=sum(1 for s in sel if forte(s)); dados=[]
for n,b,s,a,d in linhas:
    if b!=cur:
        if cur: out.append('</section>')
        u,dk=[(x[1],x[2]) for x in rotas if x[0]==b][0]
        out.append(f'<section class="bloco"><h2>{E(b)}</h2><p class="meta"><span class="cont">{sum(1 for l in linhas if l[1]==b)}</span> paradas · cerca de {fmt(dk)} km em linha reta</p><a class="rota" href="{E(u)}">Abrir a rota deste bloco no Maps</a>'); cur=b
    t=tel(s['Telefone']); _,sit=situ(s); g=grp(s['Segmento'])
    cs,ob=canais(s); lk=cs[0] if cs else None
    lkhtml='<div class="canais">'+''.join(f'<a class="cn {E(c[0][:4].lower())}" href="{E(c[2])}" target="_blank" rel="noopener"><b>{E(c[0])}</b> {E(c[1])}{f" <i>({E(c[3])})</i>" if c[3] else ""}</a>' for c in cs)+('' if cs else '<span class="cn nada">Sem site, Instagram ou WhatsApp encontrados</span>')+'</div>'+(f'<p class="obs">⚠️ {E(ob)}</p>' if ob else '')
    selo='<span class="selo">Alvo forte</span>' if forte(s) else ''
    nota=f'nota {fmt(s["Nota"])} ({mil(s["Avaliações"])} aval.)' if s['Nota'] is not None else 'sem nota'
    out.append(f'''<article id="p{n}" data-grp="{E(g)}" data-forte="{1 if forte(s) else 0}"><div class="top"><span class="n" style="background:{CORES[g]}">{n}</span><div><h3>{E(s["Nome"])} {selo}</h3><p class="meta">{E(s["Segmento"])} · {E(s["Bairro"])} · {nota} · {E(sit)}</p>{f'<p class="meta">Tel.: <span class="tel">{E(s["Telefone"])}</span></p>' if s["Telefone"] else ''}</div></div>
{lkhtml}<p class="arg">{E(a)}</p><div class="btns"><a href="{E(s["Link do Maps"])}">Ver no Maps</a>{f'<a href="{t}">Ligar</a>' if t else ''}<button type="button" class="vermapa" data-n="{n}">No mapa</button></div></article>''')
    dados.append(dict(n=n,nome=s['Nome'],g=g,lat=s['Latitude'],lon=s['Longitude'],f=1 if forte(s) else 0,info=f"{s['Segmento']} · {nota} · {sit}",maps=s['Link do Maps'],tel=t,cs=[[c[0],c[2]] for c in cs]))
out.append('</section>')
def svg_mapa():
    pts=[O]+[(d['lat'],d['lon']) for d in dados]
    la0=sum(a for a,b in pts)/len(pts); k=math.cos(math.radians(la0))
    xs=[b*k for a,b in pts]; ys=[-a for a,b in pts]
    W,H,M=600,420,26; sx=(W-2*M)/(max(xs)-min(xs)); sy=(H-2*M)/(max(ys)-min(ys)); sc=min(sx,sy)
    ox=(W-(max(xs)-min(xs))*sc)/2; oy=(H-(max(ys)-min(ys))*sc)/2
    P=lambda a,b:(round(ox+(b*k-min(xs))*sc,1),round(oy+(-a-min(ys))*sc,1))
    hx,hy=P(*O); linha=' '.join(f'{x},{y}' for x,y in [P(a,b) for a,b in pts])
    out=[f'<svg class="mapa-svg" viewBox="0 0 {W} {H}" role="img" aria-label="Mapa simplificado das lojas na ordem do roteiro">',
         f'<rect width="{W}" height="{H}" fill="#E8E4DC"/>',
         f'<polyline points="{linha}" fill="none" stroke="#172631" stroke-opacity=".45" stroke-width="2" stroke-dasharray="6 6"/>']
    # nomes dos bairros no centro de cada grupo
    grupos=collections.defaultdict(list)
    for d,s_ in zip(dados,[l[2] for l in linhas]): grupos[s_['Bairro']].append(P(d['lat'],d['lon']))
    for bairro,ps in grupos.items():
        if len(ps)<2: continue
        cx=sum(x for x,y in ps)/len(ps); cy=min(y for x,y in ps)-16
        out.append(f'<text x="{cx:.0f}" y="{max(cy,12):.0f}" text-anchor="middle" class="bairro">{E(bairro)}</text>')
    out.append(f'<g><rect x="{hx-22}" y="{hy-11}" width="44" height="22" rx="6" fill="#172631"/><text x="{hx}" y="{hy+4}" text-anchor="middle" class="casa">Casa</text></g>')
    for d in dados:
        x,y=P(d['lat'],d['lon'])
        anel=f'<circle cx="{x}" cy="{y}" r="15" fill="none" stroke="#2E6B45" stroke-width="3"/>' if d['f'] else ''
        out.append(f'<a href="#p{d["n"]}" class="pt" data-n="{d["n"]}">{anel}<circle cx="{x}" cy="{y}" r="11.5" fill="{CORES[d["g"]]}" stroke="#fff" stroke-width="2"/><text x="{x}" y="{y+4}" text-anchor="middle" class="num">{d["n"]}</text></a>')
    out.append('</svg>')
    return ''.join(out)
cg=collections.Counter(d['g'] for d in dados)
chips=''.join(f'<button type="button" class="chip" data-g="{E(g)}" aria-pressed="false"><i style="background:{CORES[g]}"></i>{E(g)} <small>{c}</small></button>' for g,c in sorted(cg.items(),key=lambda x:-x[1]))
JS=r"""
const D=__DADOS__, CASA=__CASA__, COR=__CORES__;
const sel=new Set(); let soForte=false;
const caixa=document.getElementById('mapa'); const desenho=caixa.innerHTML; let map=null;
try{ if(!window.L) throw 0; caixa.innerHTML=''; map=L.map('mapa',{zoomControl:true,tap:true}); }catch(e){ caixa.innerHTML=desenho; map=null; }
if(map){
var FUNDOS=[
 ['Ruas (Esri)','https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',{maxZoom:19,attribution:'&copy; Esri'}],
 ['Satélite (Esri)','https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',{maxZoom:19,attribution:'&copy; Esri'}],
 ['Ruas (OpenStreetMap)','https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,attribution:'&copy; OpenStreetMap'}]];
var fundo=null, falhas=0, qual=0;
var poeFundo=function(i){ if(fundo) map.removeLayer(fundo); falhas=0; qual=i;
  fundo=L.tileLayer(FUNDOS[i][1],FUNDOS[i][2]).addTo(map);
  fundo.on('tileerror',()=>{ if(++falhas>4 && qual===0) poeFundo(1); });
  const bt=document.getElementById('fundo'); if(bt) bt.textContent='Fundo: '+FUNDOS[i][0]+' · trocar'; }
poeFundo(0);
document.getElementById('fundo').addEventListener('click',()=>{ if(map) poeFundo((qual+1)%FUNDOS.length); });
var casa=L.marker(CASA,{icon:L.divIcon({className:'',html:'<div class="pin casa">Casa</div>',iconSize:[44,24],iconAnchor:[22,12]})}).addTo(map);
var linha=L.polyline([],{color:'#172631',weight:3,opacity:.55,dashArray:'6 6'}).addTo(map);
var mk={};
(__ROTULOS__).forEach(r=>L.marker([r[1],r[2]],{interactive:false,keyboard:false,icon:L.divIcon({className:'',html:'<div class="lbl">'+r[0]+'</div>',iconSize:[120,18],iconAnchor:[60,30]})}).addTo(map));
D.forEach(d=>{
  const m=L.marker([d.lat,d.lon],{icon:L.divIcon({className:'',html:`<div class="pin${d.f?' forte':''}" style="background:${COR[d.g]}">${d.n}</div>`,iconSize:[28,28],iconAnchor:[14,14]})});
  m.bindPopup(`<b>${d.n}. ${esc(d.nome)}</b><br><span class="pmeta">${esc(d.info)}</span><div class="pbtn"><a href="${d.maps}" target="_blank" rel="noopener">Ver no Maps</a>${d.tel?`<a href="${d.tel}">Ligar</a>`:''}${d.cs.map(c=>`<a href="${c[1]}" target="_blank" rel="noopener">${esc(c[0])}</a>`).join('')}<a href="#p${d.n}" class="irc">Ver cartão</a></div>`);
  mk[d.n]=m;
});
}
function esc(t){return t.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function visivel(d){return (sel.size===0||sel.has(d.g))&&(!soForte||d.f)}
function aplicar(primeira){
  const vis=D.filter(visivel); const pts=[CASA];
  D.forEach(d=>{const v=visivel(d); const el=document.getElementById('p'+d.n); el.hidden=!v; if(map){ if(v){mk[d.n].addTo(map);pts.push([d.lat,d.lon])}else{map.removeLayer(mk[d.n])} } else { const a=caixa.querySelector('.pt[data-n="'+d.n+'"]'); if(a) a.style.display=v?'':'none'; }});
  if(map) linha.setLatLngs(pts);
  document.querySelectorAll('section.bloco').forEach(s=>{const n=s.querySelectorAll('article:not([hidden])').length; s.hidden=n===0; s.querySelector('.cont').textContent=n});
  document.getElementById('total').textContent=vis.length;
  document.getElementById('vazio').hidden=vis.length>0;
  if(map){ if(pts.length>1) map.fitBounds(pts,{padding:[24,24]}); else map.setView(CASA,15); }
  document.querySelectorAll('.chip').forEach(c=>c.setAttribute('aria-pressed',sel.has(c.dataset.g)));
  document.getElementById('todos').setAttribute('aria-pressed',sel.size===0);
  document.getElementById('forte').setAttribute('aria-pressed',soForte);
}
document.querySelectorAll('.chip').forEach(c=>c.addEventListener('click',()=>{const g=c.dataset.g; sel.has(g)?sel.delete(g):sel.add(g); aplicar()}));
document.getElementById('todos').addEventListener('click',()=>{sel.clear();aplicar()});
document.getElementById('forte').addEventListener('click',()=>{soForte=!soForte;aplicar()});
document.querySelectorAll('.vermapa').forEach(b=>b.addEventListener('click',()=>{ if(!map){caixa.scrollIntoView({behavior:'smooth',block:'center'});return;} const m=mk[b.dataset.n]; document.getElementById('mapa').scrollIntoView({behavior:'smooth',block:'center'}); setTimeout(()=>{map.setView(m.getLatLng(),17);m.openPopup()},350)}));
aplicar(true);
"""
rot=collections.defaultdict(list)
for d,l in zip(dados,[l[2] for l in linhas]): rot[l['Bairro']].append((d['lat'],d['lon']))
ROT=[[b,sum(a for a,_ in v)/len(v),sum(o for _,o in v)/len(v)] for b,v in rot.items() if len(v)>=2]
JS=JS.replace('__ROTULOS__',json.dumps(ROT,ensure_ascii=False))
JS=JS.replace('__DADOS__',json.dumps(dados,ensure_ascii=False)).replace('__CASA__',json.dumps(list(O))).replace('__CORES__',json.dumps(CORES,ensure_ascii=False))
page=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Visitas 16/10</title>
<style>{LC}</style>
<style>:root{{--a:#172631;--p:#F5F2EC;--c:#2A5A7E;--l:#DDD7CC;--s:#4B5A63}}*{{box-sizing:border-box}}body{{margin:0;font-family:system-ui,sans-serif;background:var(--p);color:var(--a);line-height:1.45}}
header{{background:var(--a);color:var(--p);padding:18px 16px}}h1{{margin:0;font-size:1.4rem}}header p{{margin:4px 0 0;color:#AFC0CB;font-size:.9rem}}
main{{max-width:640px;margin:0 auto;padding:8px 16px 40px}}h2{{font-size:1.05rem;margin:24px 0 2px}}.rota{{display:block;text-align:center;background:var(--c);color:#fff;padding:12px;border-radius:10px;text-decoration:none;font-weight:700;margin:8px 0 10px}}
article{{background:#fff;border:1px solid var(--l);border-radius:12px;padding:12px 14px;margin-bottom:10px;scroll-margin-top:120px}}.top{{display:flex;gap:10px}}.n{{flex:none;width:28px;height:28px;border-radius:50%;background:var(--a);color:#fff;display:grid;place-items:center;font-weight:700;font-size:.85rem}}
h3{{margin:0;font-size:1rem}}.meta{{margin:2px 0 0;color:var(--s);font-size:.82rem}}.arg{{margin:8px 0}}.btns{{display:flex;gap:8px}}.btns a,.btns button{{flex:1;text-align:center;border:1px solid var(--c);color:var(--c);background:#fff;padding:9px 4px;border-radius:8px;text-decoration:none;font-weight:600;font:inherit;font-weight:600;cursor:pointer}}
.selo{{display:inline-block;background:#E3F1E6;color:#2E6B45;font-size:.72rem;font-weight:700;padding:2px 7px;border-radius:999px;vertical-align:2px;white-space:nowrap}}
.dica{{background:#fff;border-left:4px solid var(--c);border-radius:8px;padding:10px 12px;margin-top:12px;font-size:.92rem}}
.filtros{{position:sticky;top:0;z-index:2000;background:var(--p);padding:10px 0 8px;margin:0 -16px;padding-left:16px;padding-right:16px;border-bottom:1px solid var(--l)}}
.chips{{display:flex;gap:6px;overflow-x:auto;padding-bottom:4px;scrollbar-width:none}}.chips::-webkit-scrollbar{{display:none}}
.chip,.ctl{{flex:none;display:inline-flex;align-items:center;gap:6px;border:1px solid var(--l);background:#fff;color:var(--a);border-radius:999px;padding:7px 12px;font:inherit;font-size:.85rem;font-weight:600;cursor:pointer;white-space:nowrap;min-height:36px}}
.chip i{{width:10px;height:10px;border-radius:50%;display:inline-block}}.chip small{{color:var(--s);font-weight:500}}
.chip[aria-pressed="true"],.ctl[aria-pressed="true"]{{background:var(--a);color:#fff;border-color:var(--a)}}.chip[aria-pressed="true"] small{{color:#AFC0CB}}
.ctl.forte[aria-pressed="true"]{{background:#2E6B45;border-color:#2E6B45}}
.resumo{{font-size:.82rem;color:var(--s);margin-top:4px}}
#mapa{{position:relative;z-index:0;height:340px;border-radius:12px;border:1px solid var(--l);margin-top:12px;background:#E8E4DC}}
.pin{{width:28px;height:28px;border-radius:50%;color:#fff;display:grid;place-items:center;font-weight:700;font-size:.78rem;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.35)}}
.pin.forte{{outline:3px solid #2E6B45;outline-offset:1px}}.pin.casa{{width:44px;height:24px;border-radius:8px;background:#172631;font-size:.72rem}}
.pmeta{{color:#4B5A63;font-size:.8rem}}.pbtn{{display:flex;gap:6px;margin-top:8px;flex-wrap:wrap}}.pbtn a{{border:1px solid #2A5A7E;color:#2A5A7E;border-radius:6px;padding:5px 8px;text-decoration:none;font-weight:600;font-size:.8rem}}
.canais{{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 0}}.cn{{display:inline-flex;gap:4px;align-items:center;border-radius:999px;padding:5px 10px;font-size:.82rem;text-decoration:none;color:var(--a);background:#EEF2F5;border:1px solid var(--l);overflow-wrap:anywhere}}.cn b{{font-weight:700}}.cn i{{color:var(--s);font-style:normal;font-size:.75rem}}.cn.inst{{background:#FBEFF4;border-color:#EBC9D8}}.cn.what{{background:#E8F5EC;border-color:#C5E3CF}}.cn.nada{{color:var(--s)}}.obs{{margin:8px 0 0;font-size:.85rem;color:#8A5A00}}
.mapa-svg{{width:100%;height:100%;display:block}}.mapa-svg .num{{fill:#fff;font:700 11px system-ui,sans-serif}}.mapa-svg .casa{{fill:#fff;font:700 11px system-ui,sans-serif}}.mapa-svg .bairro{{fill:#4B5A63;font:600 12px system-ui,sans-serif}}
.lbl{{font:600 12px system-ui,sans-serif;color:#4B5A63;text-align:center;text-shadow:0 0 3px #fff,0 0 3px #fff;white-space:nowrap}}
.leg{{font-size:.8rem;color:var(--s);margin-top:6px}}
</style></head><body>
<header><h1>Visitas de 16/10</h1><p>{len(sel)} opções · {len(B)} blocos · saída do Jaraguá · {nf} alvos fortes</p></header><main>
<div class="filtros"><div class="chips" role="group" aria-label="Filtrar por segmento"><button type="button" class="ctl" id="todos" aria-pressed="true">Todos</button><button type="button" class="ctl forte" id="forte" aria-pressed="false">Só alvos fortes</button>{chips}</div>
<p class="resumo">Mostrando <b id="total">{len(sel)}</b> de {len(sel)} lojas. Toque em mais de um segmento para juntar.</p></div>
<div id="mapa" role="region" aria-label="Mapa das lojas do roteiro">{svg_mapa()}</div><button type="button" id="fundo" class="ctl" style="margin-top:8px">Fundo do mapa · trocar</button>
<p class="leg">Toque num número para ver a loja. Contorno verde = alvo forte. A linha tracejada liga as paradas na ordem do roteiro. O mapa precisa de internet. Se o fundo não aparecer, toque em "trocar".</p>
<div class="dica"><b>Não é para visitar todas.</b> A ordem leva de uma loja à vizinha mais próxima: quem não estiver ou não atender, pule para a próxima. Comece pelos <b>alvos fortes</b> (selo verde): sem site ou só rede social, nota 4,5+ e 10+ avaliações, ou ficha do Google não assumida pelo dono.</div>
<div class="dica"><b>Horários:</b> restaurante e doceria fora do almoço (prefira 9h30–11h30 e 14h30–17h); imobiliária, construtora e escritório em horário comercial; advogado costuma atender com hora marcada: peça o melhor horário para voltar.</div>
<p id="vazio" class="dica" hidden>Nenhuma loja com esse filtro. Toque em "Todos".</p>
{''.join(out)}
<p class="meta" style="margin-top:20px">Fora do roteiro: {', '.join(E(s['Nome']) for s in fora)}. Fonte: Google Maps via SerpApi (15 e 16/10/2026). A ordem usa a distância em linha reta entre as lojas; o caminho de carro pode ser maior. Mapa: © Esri e OpenStreetMap.</p></main>
<script>{LF}</script><script>{JS}</script></body></html>'''
open(SP+'Roteiro_visitas_16-10-v2.html','w').write(page)
pub=page.replace('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">','').replace('</head><body>','').replace('</body></html>','')
pub=pub.replace('<title>Visitas 16/10</title>','<title>Roteiro de visitas Pampulha</title><meta name="claude:viewport-fit-sides" content="cover">',1)
pub=pub.replace('.filtros{position:sticky;top:0;','.filtros{position:sticky;top:env(safe-area-inset-top,0px);')
pub=pub.replace('main{max-width:640px;margin:0 auto;padding:8px 16px 40px}','main{max-width:640px;margin:0 auto;padding-block:8px 40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}')
pub=pub.replace('header{background:var(--a);color:var(--p);padding:18px 16px}','header{background:var(--a);color:var(--p);padding-block:18px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:3000;background:var(--p)}')
pub=pub.replace('O mapa precisa de internet. Se o fundo não aparecer, toque em "trocar".','Toque num número para abrir a loja; arraste e use dois dedos para o zoom.')
import base64
FB=json.load(open(SP+'mapimg/fundo_bounds.json')); IMG=base64.b64encode(open(SP+'mapimg/fundo.jpg','rb').read()).decode()
ov=("var FB=[["+str(FB['S'])+","+str(FB['W'])+"],["+str(FB['N'])+","+str(FB['E'])+"]];"
    "L.imageOverlay('data:image/jpeg;base64,"+IMG+"',FB,{attribution:'&copy; OpenStreetMap'}).addTo(map);"
    "map.setMaxBounds(FB);map.options.minZoom=12;map.options.maxZoom=16;")
assert 'poeFundo(0);' in pub
pub=pub.replace('poeFundo(0);',ov,1)
pub=pub.replace('<button type="button" id="fundo" class="ctl" style="margin-top:8px">Fundo do mapa · trocar</button>','<button type="button" id="fundo" class="ctl" hidden>Fundo</button>')
pub=pub.replace('map.setView(m.getLatLng(),17)','map.setView(m.getLatLng(),16)')
import re as _re; pub=_re.sub(r"\(\[\[.*?\]\]\)\.forEach\(r=>L\.marker\(\[r\[1\],r\[2\]\].*?\.addTo\(map\)\);",'',pub,count=1)
pub=pub.replace('Mapa: © Esri e OpenStreetMap.','Mapa: © colaboradores do OpenStreetMap.')
import os; os.makedirs(SP+'pub',exist_ok=True); open(SP+'pub/roteiro-visitas.html','w').write(pub)
print('pub ok', 'filtros{position:sticky;top:env' in pub, 'padding-block:8px' in pub, 'padding-block:18px' in pub)
print('origem',O,'erro max km',round(err,3),'total km',round(tot,2))
for b,u,d in rotas: print(b,round(d,2),len(u))
print('fortes',nf, 'excluídos',[s['Nome'] for s in fora])
