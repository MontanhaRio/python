#075 - Análise de dados em uma Tupla
nu = (int(input('digite primeiro numero: ')),
      int(input('digite segundo numero: ')),
      int(input('digite terceiro numero: ')),
      int(input('digite quarto numero: ')))
print(f'voce digitou os valores {nu}')
print(f'o valor 9 apareceu na {nu.count(9)} vezes')
if 3 in nu:
    print(f'o valor 3 apareceu na {nu.index(3)+1} posicao')
else:
    print('o valor 3 nao foi digitado em nenhuma posicao')
print('os valores pares digitados foram ', end='')
for n in nu:
    if n % 2 == 0:  # % divicivel
        print(n, end=' ')
