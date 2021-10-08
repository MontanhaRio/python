#056 - Analisador completo
somaidade = 0
mesiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'-----{p} pessoa -----')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [m/f]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mesiaidade = somaidade / 4
print(f'a media de idade do grupo e de {mesiaidade} anos')
print(f'o homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'ao todo sao {totmulher20} mulheres com menos de 20 anos')

