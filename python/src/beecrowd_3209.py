
numero_de_casos = int(input())

total_de_tomadas = 0
for _ in range(numero_de_casos):
    filtros_de_linha = input().split()

    total_de_tomadas =eval('+'.join(filtros_de_linha[1:]))
    total_de_filtros = int(filtros_de_linha[0])


    total_de_aparelhos = int(total_de_tomadas) - total_de_filtros + 1

    print(total_de_aparelhos)
    