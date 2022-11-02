
numero_de_casos = int(input())

for caso in range(numero_de_casos):
    conta = input()
    if conta == 'P=NP':
        print('skipped')
    else:
        soma = eval(conta)
        print(soma)