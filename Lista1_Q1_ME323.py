'''
Código qual o número resultante de succesos X mais 
plausível de um experimento binário de n repetições 
com probabilidade de sucesso p.
Código feito por Daniel Hosomi, RA:248255
Complexidade é O(n*n)
'''
from decimal import Decimal  ### Biblioteca que garante maior precisão

def probinomial(k,n,p): ### Função que calcula a probabilidade de X=k para o experimento binário
    ans=Decimal(1)
    for j in range(k): ### For-Loop que calcula o binomial multiplicado por (p^k)
        ans=Decimal(ans*Decimal(Decimal(n-j)*p))
        ans=Decimal(ans/(j+1))
    
    for j in range(n-k): ### For-loop que multiplica o resultado anterior por ((1-p)^(n-k))
        ans=Decimal(ans*Decimal(1-p))
    
    return ans

def main():
    sum = Decimal(0)
    maior=Decimal(0)
    id=Decimal(0)   
    n = int(input()) ### n de entrada
    p = Decimal(input()) ### p de entrada

    for i in range(358,423): ### For-Loop que calcula do intervalo [0,1300]
        P=(probinomial(i,n,p))
        sum+=P
    print(sum)
    print(id, maior) ### Número X mais provável com a sua probabilidade

main()