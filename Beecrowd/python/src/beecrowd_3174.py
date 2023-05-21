
contador = 0
total_de_brinquedos = 0

horas_bonecos_somados = 0
horas_arquitetos_somados = 0 
horas_musicos_somados = 0
horas_desenhistas_somados = 0

horas_por_boneco = 8
horas_por_arquitetos = 4
horas_por_musicos = 6
horas_por_desenhistas = 12

quantidade_de_elfos = int(input())

for elfo in range(quantidade_de_elfos):
    E, G, H = input().split()
    G = G.lower()
    H = int(H)
    if G == 'bonecos':
        horas_bonecos_somados += H
    if G == 'arquitetos':
        horas_arquitetos_somados += H
    if G == 'musicos':
        horas_musicos_somados += H
    if G == 'desenhistas':
        horas_desenhistas_somados += H
    
    total_de_brinquedos =((horas_bonecos_somados // horas_por_boneco) +
    (horas_arquitetos_somados // horas_por_arquitetos) + (horas_musicos_somados // horas_por_musicos) +
    (horas_desenhistas_somados // horas_por_desenhistas))

print(total_de_brinquedos)
