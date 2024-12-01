
from escolher_dificuldade import Dificuldade

def jogar():
    dificuldade = Dificuldade()
    dificuldade.escolher_dificuldade()

    total_de_tentativas = 0
    rodada = 1

    while rodada <= 5:
        print(f"Tentativa {rodada} de 5")
        chute = int(input("Digite o seu número: "))
        print("Você digitou ", chute)
    
        numero_secreto = dificuldade.get_numero_secreto()
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

jogar()

