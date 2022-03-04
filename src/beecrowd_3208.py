
while True:
    
    fator_bom = True
    menor_fator = 0

    chave, menor_fator_exigido = map(int, input().split())

    if not chave and not menor_fator_exigido:
        break

    for contador in range(2, menor_fator_exigido):
        if chave % contador == 0:
            menor_fator = contador
            fator_bom = False
            break

    if fator_bom:
        print('GOOD')
    else:
        print(f'BAD {menor_fator}')   
        
        
