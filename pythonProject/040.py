#040 - Aquele clássico da Média
nota1 = int(input('primeira nota: '))
nota2 = int(input('segunda nota: '))
media = (nota1 + nota2) / 2
print(f'tirando {nota1:.1f} e {nota2:.1f}, a media do aluno e {media:.1f}')
if 7 > media >= 5:
    print('o aluno esta em recuperacao.')
elif media < 5:
    print('o aluno esta reprovaso.')
else:
    print('o aluno esta aprovado.')
