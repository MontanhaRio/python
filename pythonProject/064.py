#064 - Tratando vários valores v1.0
n = cont = soma = 0
n = int(input('digite um numero [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('digite um numero [999 para parar]: '))
print(f'voce digitou {cont} numero e a soma entre eles foi {soma}')
