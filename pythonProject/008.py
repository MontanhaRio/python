# km hm dam m dm cm mm
medida = float(input('uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida /10

dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f"A medida de {medida}m corresponde {km:.3f}km ")
print(f"A medida de {medida}m corresponde {hm:.3f}hm ")
print(f'A medida de {medida}m corresponde {dam:.3f}dam ')
print(f"A medida de {medida}m corresponde {dm:.0f}dm ")
print(f"A medida de {medida}m corresponde {cm:.0f}cm ")
print(f"A medida de {medida}m corresponde {mm:.0f}mm ")
