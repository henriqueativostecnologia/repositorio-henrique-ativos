# Fundo do mapa da página do celular: calcula os limites da imagem e gera uma conferência com as lojas por cima.
# A imagem é um print do embed do OpenStreetMap (ver LEIA-ME, "gerar o fundo do mapa").
#
# 1) Limites:  python3 fundo_mapa.py limites --bbox LON_O,LAT_S,LON_L,LAT_N --zoom 14 --janela 1800x1300
#    O embed desenha num zoom inteiro (em Nova Iguaçu saiu 14, não o que o bbox sugeria). A imagem cobre
#    o centro do bbox ± metade da janela, em pixels, nesse zoom (projeção Web Mercator).
# 2) Conferência:  python3 fundo_mapa.py conferir dados/config.json dados/roteiro.json dados/conferir_fundo.png
#    Desenha cada loja na imagem, nos limites da configuração. Abra o PNG e veja se lojas conhecidas
#    (um shopping, uma praça) caíram no lugar certo antes de usar o fundo. Precisa do Pillow.
import json, math, sys
def px(lat, lon, z):
    n = 256 * 2 ** z
    return (lon + 180) / 360 * n, (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * n
def geo(x, y, z):
    n = 256 * 2 ** z
    return math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n)))), x / n * 360 - 180
if sys.argv[1] == 'limites':
    a = dict(zip(sys.argv[2::2], sys.argv[3::2]))
    lo0, la0, lo1, la1 = map(float, a['--bbox'].split(',')); z = int(a['--zoom']); W, H = map(int, a['--janela'].lower().split('x'))
    x0, y0 = px(la0, lo0, z); x1, y1 = px(la1, lo1, z); cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    sw = geo(cx - W / 2, cy + H / 2, z); ne = geo(cx + W / 2, cy - H / 2, z)
    print(json.dumps({'limites_fundo': {'sudoeste': [round(sw[0], 6), round(sw[1], 6)], 'nordeste': [round(ne[0], 6), round(ne[1], 6)]}}))
elif sys.argv[1] == 'conferir':
    from PIL import Image, ImageDraw
    C = json.load(open(sys.argv[2])); R = json.load(open(sys.argv[3])); out = sys.argv[4]
    im = Image.open(C['fundo_mapa']).convert('RGB'); W, H = im.size; d = ImageDraw.Draw(im)
    (s, w), (n, e) = C['limites_fundo']['sudoeste'], C['limites_fundo']['nordeste']
    # posição na imagem em Web Mercator (a mesma conta que o Leaflet faz com o imageOverlay)
    xs, ys = px(n, w, 0); xe, ye = px(s, e, 0)
    def ponto(lat, lon):
        x, y = px(lat, lon, 0); return (x - xs) / (xe - xs) * W, (y - ys) / (ye - ys) * H
    fora = 0
    for l in R['L']:
        x, y = ponto(l['gps']['latitude'], l['gps']['longitude'])
        if not (0 <= x < W and 0 <= y < H): fora += 1; continue
        cor = (43, 95, 138) if l['grupo2'] == 'com site' else (47, 122, 79)
        d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=cor, outline=(255, 255, 255), width=2)
    x, y = ponto(*R['O']); d.rectangle([x - 9, y - 9, x + 9, y + 9], fill=(29, 43, 39), outline=(255, 255, 255), width=2)
    im.save(out); print('lojas desenhadas:', len(R['L']) - fora, '| fora da imagem:', fora, '| arquivo:', out)
