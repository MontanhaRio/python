#045 - GAME: Pedra Papel e Tesoura
from random import randint
from time import  sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opcoes:
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('qual e a sua jogada? '))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('po')
sleep(1)
print('-=' * 12)
print(f'computador jogou {itens[computador]}')
print(f'jogador jogou {itens[jogador]}')
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computedor vence')
    else:
        print('jogada invalida!')
elif computador == 1:
    if jogador == 0:
        print('computedor vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computedor vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada invalida!')
