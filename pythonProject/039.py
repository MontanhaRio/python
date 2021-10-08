#039 - Alistamento Militar
from datetime import date
atual = date.today().year
nasc = int(input('anoo de nascimento: '))
idade = atual - nasc
print(f'quem nasceu um {nasc} tem {idade} anos em {atual}.')
