#041 - Classificando Atletas
from datetime import  date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print(f'o atleta tem {idade} anos.')
if idade <= 9:
    print('clesseficacao: mirim')
elif idade <= 14:
    print('classificacao: infantil')
elif idade <= 19:
    print('classificacao juninhor')
elif idade <= 25:
    print('classificacao senior')
else:
    print('classificacao master')
    