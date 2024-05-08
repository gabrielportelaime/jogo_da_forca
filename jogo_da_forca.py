from random import randint
import os
import time

def imprimir_forca(erros, perdeu = False):
    print("{0:<15} _ {1:^20}".format(" ____", ""))
    if(perdeu):
        print("{0:<15} | {1:^20}".format("|    |", "Perdeu Playboy!"))
    else:
        print("{0:<15} | {1:^20}".format("|    |", "Palavra Secreta"))
    if(erros == 1):
        print("{0:<15} | {1:^20}".format("|    ○", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
    elif(erros == 2):
        print("{0:<15} | {1:^20}".format("|    ○", ""))
        print("{0:<15} | {1:^20}".format("|   /| ", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
    elif(erros == 3):
        print("{0:<15} | {1:^20}".format("|    ○", ""))
        print("{0:<15} | {1:^20}".format("|   /|\\", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
    elif(erros == 4):
        print("{0:<15} | {1:^20}".format("|    ○", ""))
        print("{0:<15} | {1:^20}".format("|   /|\\", ""))
        print("{0:<15} | {1:^20}".format("|    |", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
    elif(erros == 5):
        print("{0:<15} | {1:^20}".format("|    ○", ""))
        print("{0:<15} | {1:^20}".format("|   /|\\", ""))
        print("{0:<15} | {1:^20}".format("|    |", ""))
        print("{0:<15} | {1:^20}".format("|   /  ", ""))
    elif(erros == 6):
        print("{0:<15} | {1:^20}".format("|    ○", ""))
        print("{0:<15} | {1:^20}".format("|   /|\\", ""))
        print("{0:<15} | {1:^20}".format("|    |", ""))
        print("{0:<15} | {1:^20}".format("|   / \\", ""))
    else:
        print("{0:<15} | {1:^20}".format("|", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
        print("{0:<15} | {1:^20}".format("|", ""))
        print("{0:<15} | {1:^20}".format("|", ""))

arquivo = open("palavras_jogo_forca.txt", "r")
palavras = arquivo.readlines()
arquivo.close()

palavra_secreta = palavras[randint(0, len(palavras))].replace("\n", "")
chutes = []
letras_corretas = []
erros = 0
correto = 0

while True:
    os.system('cls')
    print("{0:=^50}".format(" BEM-VINDO AO JOGO DA FORCA "))
    tamanho_palavra = " A palavra secreta possui {tamanho} letras ".format(tamanho = len(palavra_secreta))
    print("{0:=^50}".format(tamanho_palavra))
    print("{0:=^50}".format(""))
    #se a posição atual corresponder a uma letra em palavra_secreta, mostra essa letra, senão, mostra um underline
    imprimir_forca(erros)
    palavra_atual = ""
    for letra in palavra_secreta:
        if letra in letras_corretas:
            palavra_atual += letra
        else:
            palavra_atual += "_"
    print("{0:<15} | {1:^20}".format("", palavra_atual))
    chute = (input("\n\nDigite uma letra: ")).lower().strip()
    #verifica se o usuário digitou de fato uma letra e a quantidade
    if chute.isalpha() != True or len(chute) != 1:
        print("Por favor, digite apenas uma letra")
        time.sleep(1)
        os.system('cls')
        continue

    #verifica se a letra digitada está no vetor de chutes, se não estiver add no mesmo
    if chute not in chutes:
        chutes.append(chute)
    else:
        print(f"Você já tentou a letra '{chute}', escolha outra")
        time.sleep(1)
        os.system('cls')
        continue

    #verifica se a letra digitada está na palavra secreta, se estiver add no vetor de letras corretas e mostra uma msg positiva, senão, mostra uma msg negativa
    for l in palavra_secreta:
        if chute == l:
            letras_corretas.append(chute)

    os.system('cls')
    if chute in palavra_secreta:
        print(f"'{chute}' faz parte da palavra secreta")
    else:
        print(f"'{chute}' não faz parte da palavra secreta")
        erros += 1

    #verifica se o jogador perdeu por tentativas
    if erros == 6:
        os.system('cls')
        print(f"Você perdeu! A palavra secreta era '{palavra_secreta.capitalize()}'\n")
        imprimir_forca(erros, True)
        break
    
    if len(letras_corretas) == len(palavra_secreta):
        os.system('cls')
        print(f"Parabéns! Você descobriu a palavra secreta '{palavra_secreta.capitalize()}'\n")
        break


