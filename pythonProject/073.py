#073 - Tuplas com Times de Futebol#073 - Tuplas com Times de Futebol
times = ('Corinthians', 'sao paulo', 'flamengo', 'Santos',
         'Cruzeiro', 'Palmeiras', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-pr', 'Bshia',
         'Gremio', 'Fluminense', 'Sport recife',
         'Ec Vitoria', 'Coritiba', 'Svsi', 'Ponte Preta',
         'atletico-go')
print('-=' * 15)
print(f'lista de times do Brasileirao: {times}')
print('-=' * 15)
print(f'os 5 primeiros sao {times[0:5]}')
print('-=' * 15)
print(f'Os ultimos sao {times[-4]}')
print('-=' * 15)
print(f'times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'o chapecoense esta na {times.index("Chapecoense")+1} posicao')
