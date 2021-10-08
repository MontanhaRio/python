#076 - Lista de Preços com Tupla
list = ('lapis', 1.90,
        'borracha', 2,
        'cardeno', 3,
        'estojo', 15.50,
        'caneta', 20)
print('-' * 40)
print(f'{"listagem de precos":^40}')
print('-' * 40)
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}', end='')
    else:
        print(f'R${list[pos]:>7.2f}')
print('-' * 40)
