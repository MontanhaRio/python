#022 - Analisador de Textos
nome = str(input('digite seu nome completo: ')).strip()
print('analisando seu nome ...')
print(f'seu nome em maiusculo e {nome.upper()}')
print(f'seu nome em minusculo e {nome.lower()}')
print(f'seu nome tem ao todo {len(nome)-nome.count(" ")} letras')
#print(f'seu primeiro nome tem {nome.find(" ")}')
separa = nome.split()
print(f'seu primeiro nome {separa[0]} e ele tem {len(separa[0])} letras')
