def movimenta(posicao_atual, movimento):
    if movimento == 1:
        valor1, valor2 = 'A', 'B'
    elif movimento == 2:
        valor1, valor2 = 'B', 'C'
    elif movimento == 3:
        valor1, valor2 = 'A', 'C'
        
    if posicao_atual == valor1:
        return valor2
    elif posicao_atual == valor2:
        return valor1
    else:
        return posicao_atual
    
if __name__ == '__main__':
    n = int(input())
    posicao_atual = input()
        
    for i in range(n):
        movimento = int(input())
        posicao_atual = movimenta(posicao_atual, movimento)

    print(posicao_atual)