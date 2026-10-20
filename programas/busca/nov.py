import sys,json;sys.path.insert(0,'.')
from serp import search
P9={'Jaraguá':(-19.8614,-43.9515),'Liberdade':(-19.8593,-43.9550),'Santa Rosa':(-19.8617,-43.9474),'Universitário':(-19.8686,-43.9468),'Dona Clara':(-19.8611,-43.9404),'Santa Cruz':(-19.8775,-43.9393),'Palmares':(-19.8729,-43.9316),'Ouro Preto':(-19.8712,-43.9841),'Bandeirantes':(-19.8587,-43.9871)}
P6={'Jaraguá+Liberdade':(-19.8604,-43.9533),'Santa Rosa+Universitário':(-19.8652,-43.9471),'Dona Clara':(-19.8611,-43.9404),'Santa Cruz+Palmares':(-19.8752,-43.9355),'Ouro Preto':(-19.8712,-43.9841),'Bandeirantes':(-19.8587,-43.9871)}
P4={'Jaraguá+Liberdade+Santa Rosa':(-19.8608,-43.9513),'Universitário+Dona Clara':(-19.8649,-43.9436),'Santa Cruz+Palmares':(-19.8752,-43.9355),'Ouro Preto+Bandeirantes':(-19.8650,-43.9856)}
P3={'Leste (Jaraguá→Palmares)':(-19.8660,-43.9440),'Oeste (Ouro Preto/Bandeirantes)':(-19.8650,-43.9856),'Norte (Santa Amélia/Itapoã)':(-19.8385,-43.9702)}
PLAN=[('revenda de carros seminovos',P3,13),('imobiliária',P6,15),('construtora',P3,13),('advogado trabalhista',P4,15),('advogado previdenciário',P4,15),('doceria',P6,15),('restaurante',P9,15)]
MES0=207; n=0
for q,P,z in PLAN:
  for nome,(la,lo) in P.items():
    if 250-(MES0+n)<=5: print('PARADA: saldo do mês chegou a 5'); sys.exit()
    d=search(dict(engine='google_maps',type='search',q=q,ll=f'@{la},{lo},{z}z',hl='pt-br',gl='br')); n+=1
    print(q,'|',nome,'|',len(d.get('local_results',[]) or []), d.get('error',''))
print('buscas',n)
