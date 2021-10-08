import qrcode
#criando 1 qrcode
#imagem_qrcode = qrcode.make('https://pt.wikipedia.org/wiki/Microsoft_Excel')
#imagem_qrcode.save('qrcode/qrcode_python.png')

#criando varios qrcode de 1 vez
link_produtos = {
    'Exvel': 'https://pt.wikipedia.org/wiki/Microsoft_Excel',
    'VBA': 'https://docs.microsoft.com/pt-br/office/vba/library-reference/concepts/getting-started-with-vba-in-office',
    'power BI': 'https://powerbi.microsoft.com/pt-br/',
    'Python': 'https://ieee.org.cy/events-activities/programming-course-series-01-introductory-course-to-python/'

}
for produto in link_produtos:
    link = link_produtos[produto]
    imagem_qrcode = qrcode.make('link')
    imagem_qrcode.save(f'qrcode/qrcode_{produto}.png')
