import random
import time

def criartabuleiro(altura,largura):
    tabuleiro = []

    for i in range(altura):
        tabuleiro.append(largura*[0])

    return tabuleiro


def mostrarcampo(campo):

    for contador in range(5):
        print(campo[contador])


acertos1=0
acertos2=0

campoaliado = criartabuleiro(5,10)
campoinimigo = criartabuleiro(5,10)
campovisao = criartabuleiro(5,10)

for cont in range(5):
    linha=int(input("Digite em qual linha quer posicionar seu navio de 1 a 5:"))-1
    coluna=int(input("Digite em qual coluna quer posicionar seu navio de 1 a 10: "))-1
    campoaliado[linha][coluna]=1
    print("Campo aliado")
    mostrarcampo(campoaliado)

for contas in range(5):
    linha1=random.randint(0,4)
    coluna1=random.randint(0,9)
    campoinimigo[linha1][coluna1]=1

while acertos1<5 and acertos2<5:
    linha2=int(input("Digite a linha que deseja atacar de 1 a 5:")) - 1
    coluna2=int(input("Digite qual coluna deseja atacar de 1 a 10:")) - 1

    if campoinimigo[linha2][coluna2] == 1:
        acertos1=acertos1+1
        print("Você acertou!!!")
        campoinimigo[linha2][coluna2]=0
        campovisao[linha2][coluna2]="A"
        mostrarcampo(campovisao)
    else:
        print("Você errou.   :(")
        campovisao[linha2][linha2]="X"
        mostrarcampo(campovisao)

    linha3=random.randint(0,4)
    coluna3=random.randint(0,9)

    if campoaliado[linha3][coluna3]==1:
        time.sleep(4)
        print("O inimigo abateu um de nossos navis.")
        acertos2 = acertos2 + 1
        campoaliado[linha3][coluna3] = "A"
        print("Campo aliado")
        mostrarcampo(campoaliado)
    else:
        time.sleep(4)
        campoaliado[linha3][coluna3] = "X"
        print("O inimigo errou!!!")
        print("Campo aliado")
        mostrarcampo(campoaliado)

if acertos1 == 5:
    print("Parabens você ganhou")

elif acertos2 == 5:
    print("Você perdeu :(")
