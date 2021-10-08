#070 - Estatísticas em produtos
total = totmil = 0
while True:
    p = str(input('nome do produto: '))
    pr = float(input('preco: R$ '))
    total += pr
    if pr > 1000:
        totmil += 1
    res = ' '
    while res not in 'SN':
        res = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'o total da compra foi R$ {total:.2f}')
print(f'temos {totmil} produtos custando mais de R$ 1000.00 ')
