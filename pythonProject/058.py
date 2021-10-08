#058 - Jogo da Adivinhação v2.0
from random import  randint
computador = randint(0, 10)
print('sou seu computador ... acabei de pensar em um numero entre 0 e 10. ')
print('sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual e seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais ... tente mais uma vez.')
        elif jogador > computador:
            print('menos... tente mais uma vez.')
print(f'acertou com {palpites} tentativas. parabens!')
