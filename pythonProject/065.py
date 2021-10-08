#065 - Maior e Menor valores
resp = 'S'
soma = maior = menor = quant = media = 0
while resp in 'Ss':
    n = int(input('digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'voce digitou {quant} numero e a media foi {media}')
print(f'o maior valor foi {maior} e o menor foi {menor}')
