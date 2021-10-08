#044 - Gerenciador de Pagamentos
print(f' {" lojas victor ":=^40} ')
preco = float(input('preco das compras: R$ '))
print('''formas de pagamento
[1] a vista dinheiro
[2] a vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
opcao = int(input('qual e a apcao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco = (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'sua compra sera parcelada em 2x de R$ {parcela:.2f} sem juros')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('quantas parcelas? '))
    parcelas = total / totparc
    print(f'sua compra sera parcelada em {totparc}x de R$ {parcelas:.2f} com juros')
else:
    total = preco
    print('opcao invalida de pagamento')
print(f'sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final')
