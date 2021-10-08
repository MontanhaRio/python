#037 - Conversor de Bases Numéricas
num = int(input('digite um numero inteiro: '))
print('''escolha uma das bases para conversao:
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')
opcao = int(input('sua opcao: '))
if opcao == 1:
    print(f'{num} convertido para binario e igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal e igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal e igual a {hex(num)[2:]}')
else:
    print('opcao invalida. tente novamente.')
