#071 - Simulador de Caixa Eletrônico
print('=-' * 20)
print(' {:~^30} '.format(' banco kenji '))
print('=-' * 20)
valor = int(input('que valor vocr quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'total de {totced:2} cedulas de R$ {ced:2}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break