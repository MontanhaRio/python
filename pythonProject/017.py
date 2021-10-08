from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adiacente; '))
hi = hypot(co, ca)
print(f'a hipotenusa vai medir {hi:.2f}')
# (co ** 2 + ca ** 2) ** (1/2) formula da hipotenusa
#Catetos e Hipotenusa