''' Jogo de Adivinhação '''

import random

def jogar() :

    print("#################################")
    print("Bem vindo ao jogo de Adivinhação!")
    print("#################################")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) fácil, (2) médio, (3) difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1) :
        total_de_tentativas = 20
    elif(nivel == 2) :
        total_de_tentativas = 10
    else :
        total_de_tentativas = 3


    for rodada in range(1, total_de_tentativas + 1) :
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou", chute)

        if(chute < 1 or chute > 100) :
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou) :
            print("Você acertou!! E fez {} pontos!".format(pontos))
            break
        else : 
            if(maior) :
                print("Você errou! O seu chute foi maior que o número secreto.")
                if (rodada == total_de_tentativas) :
                    print("O número secreto era {}, e você fez {} pontos".format(numero_secreto, pontos))
            elif(menor) :
                print("Você errou! O seu chute foi menor que o número secreto.")
                if (rodada == total_de_tentativas) :
                    print("O número secreto era {}, e você fez {} pontos".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    
    
    print("Fim do jogo")

    #print(type(chute_str))
    #print(numero_secreto)

if(__name__ == "__main__") :
    jogar()
