#061 - Progressão Aritmética v2.0
primeiro = int(input('primeiro termo: '))
razao = int(input('razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo += razao
    cont += 1
print('FIM')
