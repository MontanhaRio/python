#057 - Validação de Dados
sexo = str(input('informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos. por favor, informe seu sexo: ')).strip().upper()[0]
print(f'sexo {sexo} registrado com secesso ')


