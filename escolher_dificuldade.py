import random

class Dificuldade:
    def __init__(self):
        self.numero_secreto = None

    def escolher_dificuldade(self):
        print('\n \t DIFICULDADES \n')
        print('1. 1-10')
        print('2. 1-100')
        print('3. 1-1000')
        while True:
            dificuldade = int(input("Selecione a dificuldade: "))
            if dificuldade == 1:
                self.numero_secreto = random.randint(1, 10)
                print('Você deve advinhar um número entre 1-10')
                break
            elif dificuldade == 2:
                self.numero_secreto = random.randint(1, 100)
                print("Você deve adivinhar um número entre 1 e 100.")
                break
            elif dificuldade == 3:
                self.numero_secreto = random.randint(1, 1000)
                print("Você deve adivinhar um número entre 1 e 1000.")
                break
            else:
                print('Dificuldade inválida, tente novamente.')

    def get_numero_secreto(self):
        return self.numero_secreto