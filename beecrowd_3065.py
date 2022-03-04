j = 1
total = 0
sinal = []

while int(input()) != 0:
    calc = input()
    calc2 = calc.replace('+', ' ').replace('-', ' ').split()

    for m in range(len(calc2)):
        calc2[m] = int(calc2[m])

    for i in range(len(calc)):
        if calc[i] == '+':
            sinal.append('+')
        elif calc[i] == '-':
            sinal.append('-')

    total = calc2[0]

    k = 0
    while k < len(sinal):
        if sinal[k] == '+':
            total += calc2[k+1]
        elif sinal[k] == '-':
            total -= calc2[k+1]
        k += 1

    print(f'Teste {j}')
    print(total)
    print()
    j += 1
    calc2 = []
    sinal = []