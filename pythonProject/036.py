#036 - Aprovando Empréstimo
casa = float(input('valor da casa: R$ '))
salario = float(input('salario do comprador: R$ '))
anos = int(input('quantos anos de financiamento? '))
prestacao  = casa / (anos * 12)
print(f'para pagar uma casa de R$ {casa:.2f} em {anos}')
print(f'a prestacao sera de R$ {prestacao:.2f}')
