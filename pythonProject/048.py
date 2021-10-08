#048 - Soma ímpares múltiplos de três
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'a soma de todos os {cont} valores solicitados e {soma}')

