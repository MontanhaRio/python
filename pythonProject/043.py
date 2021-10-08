altura = float(input('qual sua altura? (m) '))
peso = float(input('qual seu peso ? (kg) '))
imc = peso / (altura ** 2)
print(f'O imc dessa pessoa e de {imc:.1f}')
if imc < 18.5:
    print('voce esta abaixo do peso ')
elif 18.5 <= imc < 25:
    print('voce esta com peso normal')
elif 25 <= imc < 30:
    print('voce esta em sobrepeso')
elif 30 <= imc <40:
    print('voce esta em obesidade')
elif imc >= 40:
    print('voce esta em obesidade morbida, cuidado')