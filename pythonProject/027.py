#027 - Primeiro e último nome de uma pessoa
n = str(input('digite seu nome completo:')).strip()
nome =  n.split()
print('multo przer em te conhecer! ')
print(f'seu primeiro nome e {nome[0]}')
print(f'seu ultimo nome e {nome[len(nome)-1]}')
