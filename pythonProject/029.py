#029 - Radar eletrônico
v = float(input('qual e a velocidade atual do carro? '))
if v > 80:
    print('multado! voce excedeu o limiti permitido que e de 80km/h')
    multa = (v-80) * 7
    print(f'voce deve pagar uma multa de R${multa:.2f}!')
print('tenha um bom dia ! dirija com seguranca!')
