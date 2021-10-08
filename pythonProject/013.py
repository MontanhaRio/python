salario = float(input('qual e o salario do funcionario? R$ '))
novo = salario + (salario * 15 / 100)
print(f'um funcionario que ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}')
