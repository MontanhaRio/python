#042 - Analisando Triângulos v2.0
r1 =float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar um triangulo! ', end='')
    if r1 == r2 == r3:
        print('equilatero!')
    elif r1 != r2 != r3 != r1:
        print('escaleno!')
    else:
        print('isosceles')
else:
    print('os segmentos acima nao podem formar triangulo')
