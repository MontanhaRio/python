#069 - Análise de dados do grupo
tot18 = toth = totm20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'total de pessoas com mais de 18 anos: {tot18}')
print(f'ao todo temos {toth} homens cadastrados')
print(f'e temos {totm20} mulheres com menos de 20 anos')
