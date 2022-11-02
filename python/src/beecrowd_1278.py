tem_caso_anterior = False

while True:
    quantidade_de_linhas = int(input())

    if not quantidade_de_linhas:
        break
    if tem_caso_anterior:
        print() # Adicionando uma quebra de linha entre os casos

    texto = [] # Onde será armazenado o texto de cada caso

    for linha in range(quantidade_de_linhas):
        texto.append(' '.join(input().split())) # Fazendo o input e acrescentando na lista 'texto'

    # Descobrindo a maior linha do texto com função 'max()'
    maior_linha_do_texto = max(len(linha) for linha in texto) 
  
    for linha in range(len(texto)):
        # Adicionando espaços em branco em cada linha para deixar o texto formadado,
        # de acordo com a maior linha do texto.
        for _ in range(maior_linha_do_texto-len(texto[linha])):
            print('', end=' ')
        # Imprimindo linha depois de adicionar os espaços necessarios
        print(texto[linha])

    tem_caso_anterior = True