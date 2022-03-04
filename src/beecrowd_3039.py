
numero_de_criancas = int(input())

contador_carrinhos = 0
contador_bonecas = 0

for crianca in range(numero_de_criancas):
    nome, genero = input().split()
    if genero.upper() == 'M':
        contador_carrinhos += 1
        
    elif genero.upper() == 'F':
        contador_bonecas +=1

print(f"{contador_carrinhos} carrinhos")
print(f"{contador_bonecas} bonecas")

