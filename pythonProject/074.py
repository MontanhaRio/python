#074 - Maior e menor valores em Tupla
from random import  randint
n1 = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os valores sorteados foram: ', end='')
for n in n1:
    print(f'{n} ', end='')
print(f'\no maior valor sorteado foi {max(n1)}')
print(f'O menor valor sorteado foi {min(n1)}')
