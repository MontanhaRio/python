#028 - Jogo da Adivinhação v.1.0
from random import randint
from time import sleep
computador = randint(0, 5)# faz computador pensar
print('-=-' *20)
print('vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
jogador = int(input('em que numero eu pensei? '))# jogado tenta adivinhar
print('processando..')
sleep(3)
if jogador == computador:
    print('parabens voce conseguiu me vencer!')
else:
    print(f'ganhei eu pensei no numero {computador} e nao no {jogador}')
