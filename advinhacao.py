
import random
from escolher_dificuldade import dificuldade
numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
rodada = 1

print("Bem-vindo ao jogo de adivinhação!")

dificuldade()

while rodada <= 5:
    print(f"Tentativa {rodada} de 5")
    chute = input("Digite o seu número: ")
    print("Você digitou ", chute)
   

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor que o número secreto.")
    rodada = rodada + 1

print("Fim do jogo")

