import openpyxl


wb = openpyxl.Workbook()


sh = wb.active

sh['A1'] = 'programa'

sh['B1'] = 'python'

wb.save(filename = 'teste/teste.xlsx')
