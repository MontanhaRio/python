#031 - Custo da Viagem
dis = float(input('qual e a distancia da sua viagem? '))
print(f'voce esta preste a comecar uma viagem de {dis}km.')
p = dis * 0.50 if dis <= 200 else dis * 0.45
print(f'e o preco da sua passagem sera de R${p:.2f}')

