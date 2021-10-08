#059 - Criando um Menu de Opções
from time import sleep
n1 = int(input('primero valor: '))
n2 = int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opcao = int(input('>>>>>>>qual e a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'a soma de {n1} + {n2} e {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'o resultado de {n1} * {n2} e {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'entre {n1} e {n2} o maior e {maior}')
    elif opcao == 4:
        print('informe os numeros novamente:')
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif opcao == 5:
        print('finalizado...')
    else:
        print('opcao invalida. tente novamente')
    print('=-=' * 10)
    sleep(2)
print('fim do programa! volte sempre!')
