contador_de_casos = 1
total_da_expressao = 0
sinais_da_expressao = []

while int(input()) != 0:
    calculo_para_ser_realizado = input()
    calculo_sem_os_sinais = calculo_para_ser_realizado.replace('+', ' ').replace('-', ' ').split()

    for numero in range(len(calculo_sem_os_sinais)):
        calculo_sem_os_sinais[numero] = int(calculo_sem_os_sinais[numero])

    for sinal in range(len(calculo_para_ser_realizado)):
        if calculo_para_ser_realizado[sinal] == '+':
            sinais_da_expressao.append('+')
        elif calculo_para_ser_realizado[sinal] == '-':
            sinais_da_expressao.append('-')

    total_da_expressao = calculo_sem_os_sinais[0]

    posicao = 0
    while posicao < len(sinais_da_expressao):
        if sinais_da_expressao[posicao] == '+':
            total_da_expressao += calculo_sem_os_sinais[posicao+1]
        elif sinais_da_expressao[posicao] == '-':
            total_da_expressao -= calculo_sem_os_sinais[posicao+1]
        posicao += 1

    print(f'Teste {contador_de_casos}')
    print(total_da_expressao)
    print()
    contador_de_casos += 1
    calculo_sem_os_sinais = []
    sinais_da_expressao = []