#026 - Primeira e última ocorrência de uma string
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")}')
print(f'A primeira letra A apareeceu na posicao {frase.find("A")+1}')
print(f'A ultima letra A aparece na posicao {frase.rfind("A")+1}')
