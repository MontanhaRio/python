#066 - Vários números com flag
s = cont = 0
while True:
    n = int(input('digite um valor [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'a soma dos {cont} valores foi {s}')
