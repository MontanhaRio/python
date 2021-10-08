#033 - Maior e menor valores
a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
c = int(input('terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O mairor valor digitado foi {maior}')