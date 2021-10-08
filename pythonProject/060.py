#060 - Cálculo do Fatorial
from math import factorial
n = int(input('digite um numero para calcular seu fatorial: '))
#f = factorial(n)
c = n
f = 1
print(f'calculando {n}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
