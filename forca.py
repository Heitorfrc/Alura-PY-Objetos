''' Jogo da Forca '''

import random

def jogar() :

    imprime_mensagem_abertura()

    palavra_secreta = cria_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou) :

        chute = pede_chute()
        
        if(chute in palavra_secreta) :
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else :
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou) :
        imprime_mensagem_vencedor(palavra_secreta)
    else :
        imprime_mensagem_perdedor(palavra_secreta)



def imprime_mensagem_abertura() :
    print("#################################")
    print("## Bem vindo ao jogo da Forca! ##")
    print("#################################")

def cria_palavra_secreta() :
    arquivo = open("palavras.txt", "r")
    
    palavras = []

    for linha in arquivo :
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close() #palavras.txt FECHADO

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra) :
    return ["_" for letra in palavra]

def pede_chute() :
    chute = input("Qual a letra?")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta) :
    index = 0
    for letra in palavra_secreta :
        if(chute == letra) :
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros) :

    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()    

def imprime_mensagem_vencedor(palavra_secreta) :
    print("{}!!".format(palavra_secreta))
    print("Parabéns você acertou a palavra!!")

def imprime_mensagem_perdedor(palavra_secreta) :
    print("Forca!")
    print("A palavra era {}".format(palavra_secreta))


if(__name__ == "__main__") :
    jogar()
