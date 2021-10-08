#062 - Super Progressão Aritmética v3.0
print('gerador de PA')
print('-=' * 10)
p = int(input('primeiro termo: '))
r = int(input('razao da PA: '))
t = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{t} - ', end='')
        t += r
        cont += 1
    print('pausa')
    mais = int(input('quantos termos voce quer mostrar a mais? '))
print(f'progresso finalizada com {total} termos mostrados:')

