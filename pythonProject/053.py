#053 - Detector de Palíndromo
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print(f'o inveso de {junto} e {inverso}')

'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''

if inverso == junto:
    print('temos um palindromo!')
else:
    print('a frase digitada nao e um palindromo')

