import random
### Biblioteca responsável por gerar números aleatórios
def main():
    totalA=0
    totalB=0
    total0=0
    totalQ=0
    E=0
    V=0
    PA=0
    PB=0
    P0=0
    X=[]
    while totalA+totalB+total0<1000000: ### Simular o evento 1 milhão de vezes
        A=50
        B=20
        num=0
        while A!=0 and B!=0: ### Simulador do Evento
            win=random.randint(1,2)
            num+=1
            if win<2:
                A+=1
                B-=1
            else:
                A-=1
                B+=1
            if num>10000000: ### Vamos considerar que o jogo não acabo se ele tem mais de 10 milhões de lances
                total0+=1
                break

        X.append(num)
        totalQ+=num
        if A!=0 and B==0:
            totalA+=1
        elif B!=0 and A==0:
            totalB+=1

    E=totalQ/(totalA+totalB) ### Esperança é a média do numero total de jogadas
    PA=totalA/(totalA+totalB)
    PB=totalB/(totalB+totalA)
    P0=total0/(totalA+totalB)
    for x in X: ### Cálculo da Variância
        V+=(x-E)*(x-E)
    V/=(totalA+totalB)

    print("E de N é =",E)
    print("X de N é =",V)
    print("Probabilidade do jogo não acabar é =",P0)
    print("Probabilidade de A ganhar é =",PA)
    print("Probabilidade de B ganhar é =",PB)

main()

### Item A
### P1 ganhar 0,71428571428571428571428571428571 e P2 ganhar 0,28571428571428571428571428571429
### Resultados gerados pelo Programa: P1 = 0.714472 e P2 = 0.285528

### Item B
### A probabilidade é 0, pois, o jogo sempre termina.

### Item C
### E = 1000.30568
### V = 964743.6771051893

### Item D
### P2 ganhar 0.5863623946359614 e P1 ganhar 0.4136376053640386
### Resultados gerados pelo Programa: P1 = 0.414708 e P2 = 0.585292