import openpyxl

#Criar uma planilha(book)
book = openpyxl.Workbook()

#Criar uma pagina
book.create_sheet('Frutas')
#Como selecionar uma pagina
f = book['Frutas']
f.append(['Frutas', 'Quantidades', 'Preço'])
f.append(['fruta 1', '5', 'R$5,00'])
f.append(['fruta 2', '2', 'R$15,00'])
f.append(['fruta 3', '10', 'R$30,00'])
f.append(['fruta 4', '53', 'R$50,00'])

book.save('compra.xlsx')