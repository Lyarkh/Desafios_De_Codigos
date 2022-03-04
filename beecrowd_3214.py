
E, F, C = map(int, input().split())

G = E + F
resposta = 0

while G >= C:
    resposta += G // C
    G = G // C + G % C
print(resposta)

