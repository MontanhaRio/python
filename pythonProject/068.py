#068 - Jogo do Par ou Ímpar
from random import randint
v = 0
while True:
    jogador = int(input('digite um valor: '))
    com = randint(0, 10)
    total = jogador + com
    tipu = ' '
    while tipu not in 'PI':
        tipu = str(input('voce quer PAR ou IMPAR? [P/I]')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {com} o total e {total}')
    if tipu == 'P':
        if total % 2 == 0:
            print('voce ganhou! ')
            v += 1
        else:
            print('voce perdeu!')
    if tipu == 'I':
        if total % 2 == 1:
            print('voce ganhou!')
            v += 1
        else:
            print('voce perdeu!')
            break
    print('vamos jogar novamente...')
print(f'GAME OVER! voce ganhou {v} vezes! ')
