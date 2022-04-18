'''
Programa responsável por determinar quantas plantas ganharam do grupo de tratamento
'''
from sys import argv

def main():
    entrada=argv[1]
    saida=argv[2]
    vetor=[]

    expsum=0
    normsum=0

    with open(entrada) as arquivo:
        for i in arquivo.readlines():
            num, iT1, iT2, prod1, prod2 = i.split()
            num=int(num)
            iT1=int(iT1)
            iT2=int(iT2)
            prod1=float(prod1)
            prod2=float(prod2)
            if (iT1==1 and prod1>prod2) or (iT2==1 and prod2>prod1):
                expsum+=1
                vetor.append(f"Em {num} a planta do experimento ganhou.\n")
            else:
                normsum+=1
                vetor.append(f"Em {num} a planta do experimento perdeu.\n")

    with open(saida,"w") as arquivo:
        print(expsum, normsum,file=arquivo) 
        print(expsum/(normsum+expsum),file=arquivo)
        print("".join(vetor),file=arquivo)

main()