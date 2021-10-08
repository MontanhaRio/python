from barcode import EAN13
from barcode import writer
from barcode.writer import ImageWriter

#codigo_barra = EAN13('123123123123', writer=ImageWriter())
#codigo_barra.save('codigo_barra')

codigo_produtos = {
    'Feijao': '551765111111',
    'Arroz': '665798011111',
    'MAcarrao': '665887111111',
    'Azeite': '9985562111111'
}
for produto in codigo_produtos:
    codigo = codigo_produtos[produto]
    codigo_barra = EAN13(codigo, writer=ImageWriter())
    codigo_barra.save(f'barcode/codigo_barra_{produto}')